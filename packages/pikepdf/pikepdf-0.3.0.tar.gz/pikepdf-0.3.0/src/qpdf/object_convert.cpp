/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * Copyright (C) 2017, James R. Barlow (https://github.com/jbarlow83/)
 */

/*
 * Convert Python types <-> QPDFObjectHandle types
 */

#include <vector>
#include <map>

#include <qpdf/Constants.h>
#include <qpdf/Types.h>
#include <qpdf/DLL.h>
#include <qpdf/QPDFExc.hh>
#include <qpdf/QPDFObjGen.hh>
#include <qpdf/PointerHolder.hh>
#include <qpdf/Buffer.hh>
#include <qpdf/QPDFObjectHandle.hh>
#include <qpdf/QPDF.hh>
#include <qpdf/QPDFWriter.hh>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "pikepdf.h"


std::map<std::string, QPDFObjectHandle>
dict_builder(py::dict dict)
{
    StackGuard sg(" dict_builder");
    std::map<std::string, QPDFObjectHandle> result;

    for (auto item: dict) {
        std::string key = item.first.cast<std::string>();

        auto value = objecthandle_encode(item.second);
        result[key] = value;
    }
    return result;
}

std::vector<QPDFObjectHandle>
array_builder(py::iterable iter)
{
    StackGuard sg(" array_builder");
    std::vector<QPDFObjectHandle> result;
    int narg = 0;

    for (auto item: iter) {
        narg++;

        auto value = objecthandle_encode(item);
        result.push_back(value);
    }
    return result;
}


QPDFObjectHandle objecthandle_encode(py::handle handle)
{
    if (handle.is_none())
        return QPDFObjectHandle::newNull();

    // Ensure that when we return QPDFObjectHandle/pikepdf.Object to the Py
    // environment, that we can recover it
    try {
        auto as_qobj = handle.cast<QPDFObjectHandle>();
        return as_qobj;
    } catch (py::cast_error) {}

    // Special-case booleans since pybind11 coerces nonzero integers to boolean
    if (py::isinstance<py::bool_>(handle)) {
        bool as_bool = handle.cast<bool>();
        return QPDFObjectHandle::newBool(as_bool);
    }

    auto Decimal = py::module::import("decimal").attr("Decimal");

    if (py::isinstance(handle, Decimal)) {
        return QPDFObjectHandle::newReal(py::str(handle));
    } else if (py::isinstance<py::int_>(handle)) {
        auto as_int = handle.cast<long long>();
        return QPDFObjectHandle::newInteger(as_int);
    } else if (py::isinstance<py::float_>(handle)) {
        auto as_double = handle.cast<double>();
        return QPDFObjectHandle::newReal(as_double);
    }

    py::object obj = py::reinterpret_borrow<py::object>(handle);

    if (py::isinstance<py::bytes>(obj)) {
        py::bytes py_bytes = obj;
        return QPDFObjectHandle::newString(static_cast<std::string>(py_bytes));
    } else if (py::isinstance<py::str>(obj)) {
        // First check if we can encode the string as ASCII
        auto as_ascii = py::reinterpret_steal<py::bytes>(
            PyUnicode_AsEncodedString(obj.ptr(), "ascii", nullptr));
        if (as_ascii) {
            std::string ascii = static_cast<std::string>(as_ascii);
            return QPDFObjectHandle::newString(ascii);
        }
        PyErr_Clear();

        // ...and if ASCII fails, we have to encode as UTF-16BE with
        // byte order marks packed in a std::string. Including any NULs that
        // may appear.
        auto as_utf16 = py::reinterpret_steal<py::bytes>(
            PyUnicode_AsEncodedString(obj.ptr(), "utf-16be", nullptr));
        if (!as_utf16) {
            // Still can't encode it, so toss the error back
            throw py::error_already_set();
        }
        auto utf16 = static_cast<std::string>(as_utf16);
        // Put the utf-16be string in a regular std::string... that is what
        // QPDF wants
        auto utf16_encoded = std::string("\xfe\xff") + utf16;
        return QPDFObjectHandle::newString(utf16_encoded);
    }

    if (py::hasattr(obj, "__iter__")) {
        //py::print(py::repr(obj));
        bool is_mapping = false; // PyMapping_Check is unreliable in Py3
        if (py::hasattr(obj, "keys"))
            is_mapping = true;

        bool is_sequence = PySequence_Check(obj.ptr());
        if (is_mapping) {
            return QPDFObjectHandle::newDictionary(dict_builder(obj));
        } else if (is_sequence) {
            return QPDFObjectHandle::newArray(array_builder(obj));
        }
    }

    throw py::cast_error(std::string("don't know how to encode value ") + std::string(py::repr(obj)));
}


py::object decimal_from_pdfobject(QPDFObjectHandle& h)
{
    auto decimal_constructor = py::module::import("decimal").attr("Decimal");

    if (h.getTypeCode() == QPDFObject::object_type_e::ot_integer) {
        auto value = h.getIntValue();
        return decimal_constructor(py::cast(value));
    } else if (h.getTypeCode() == QPDFObject::object_type_e::ot_real) {
        auto value = h.getRealValue();
        return decimal_constructor(py::cast(value));
    } else if (h.getTypeCode() == QPDFObject::object_type_e::ot_boolean) {
        auto value = h.getBoolValue();
        return decimal_constructor(py::cast(value));
    }
    throw py::type_error("object has no Decimal() representation");
}
