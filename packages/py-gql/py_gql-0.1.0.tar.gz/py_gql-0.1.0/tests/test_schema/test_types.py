# -*- coding: utf-8 -*-
""" Test type definition classes """

import re
import uuid

import pytest

from py_gql.exc import (
    ScalarParsingError,
    ScalarSerializationError,
    UnknownEnumValue,
)
from py_gql.lang.parser import parse_value
from py_gql.schema import UUID, Boolean, EnumType, Float, Int, RegexType, String


def test_EnumType_rejects_duplicate_names():
    with pytest.raises(AssertionError):
        EnumType("Enum", [("SOME_NAME", 1), ("SOME_NAME", 2)])


@pytest.mark.parametrize("name", ["null", "true", "false"])
def test_EnumValue_rejects_forbidden_name(name):
    with pytest.raises(AssertionError):
        EnumType("Enum", [name])


def test_EnumType_get_value_ok():
    t = EnumType("Enum", [("SOME_NAME", 1)])
    assert t.get_value("SOME_NAME") == 1


def test_EnumType_get_value_fail():
    t = EnumType("Enum", [("SOME_NAME", 1)])
    with pytest.raises(UnknownEnumValue) as exc_info:
        t.get_value("SOME_OTHER_NAME")
    assert str(exc_info.value) == "Invalid name SOME_OTHER_NAME for enum Enum"


def test_EnumType_get_name_ok():
    t = EnumType("Enum", [("SOME_NAME", 1)])
    assert t.get_name(1) == "SOME_NAME"


def test_EnumType_get_name_fail():
    t = EnumType("Enum", [("SOME_NAME", 1)])
    with pytest.raises(UnknownEnumValue) as exc_info:
        t.get_name(2)
    assert str(exc_info.value) == "Invalid value 2 for enum Enum"


@pytest.mark.parametrize(
    "type, input, output",
    [
        (Int, 1, 1),
        (Int, "123", 123),
        (Int, 0, 0),
        (Int, -1, -1),
        (Int, 1e5, 100000),
        (Int, False, 0),
        (Int, True, 1),
        (Float, 1, 1.0),
        (Float, 0, 0.0),
        (Float, "123.5", 123.5),
        (Float, -1, -1.0),
        (Float, 0.1, 0.1),
        (Float, 1.1, 1.1),
        (Float, -1.1, -1.1),
        (Float, "-1.1", -1.1),
        (Float, False, 0.0),
        (Float, True, 1.0),
        (String, "string", "string"),
        (String, 1, "1"),
        (String, -1.1, "-1.1"),
        (String, True, "true"),
        (String, False, "false"),
        (Boolean, "string", True),
        (Boolean, "", False),
        (Boolean, 1, True),
        (Boolean, 0, False),
        (Boolean, True, True),
        (Boolean, False, False),
    ],
)
def test_scalar_serialization_ok(type, input, output):
    assert type.serialize(input) == output


@pytest.mark.parametrize(
    "type, input, err",
    [
        (Int, 0.1, "Int cannot represent non-integer value: 0.1"),
        (Int, 1.1, "Int cannot represent non-integer value: 1.1"),
        (Int, -1.1, "Int cannot represent non-integer value: -1.1"),
        (Int, "-1.1", "Int cannot represent non-integer value: -1.1"),
        (
            Int,
            9876504321,
            "Int cannot represent non 32-bit signed integer: 9876504321",
        ),
        (
            Int,
            "-9876504321",
            "Int cannot represent non 32-bit signed integer: -9876504321",
        ),
        (Int, "1e100", "Int cannot represent non 32-bit signed integer: 1e100"),
        (Int, "-1e100", "Int cannot represent non-integer value: -1e100"),
        (Int, "one", "Int cannot represent non-integer value: one"),
        (
            Int,
            "",
            "Int cannot represent non 32-bit signed integer: (empty string)",
        ),
        (Int, None, "Int cannot represent non 32-bit signed integer: None"),
        (Float, None, "Float cannot represent non numeric value: None"),
        (Float, "one", "Float cannot represent non numeric value: one"),
        (Float, "", "Float cannot represent non numeric value: (empty string)"),
    ],
)
def test_scalar_serialization_fail(type, input, err):
    with pytest.raises(ScalarSerializationError) as exc_info:
        type.serialize(input)
    assert str(exc_info.value) == err


class TestUUID(object):
    def test_parse_string(self):
        assert UUID.parse("c4da8450-ec7a-4d3b-9ade-18194daeb2d6") == uuid.UUID(
            "c4da8450-ec7a-4d3b-9ade-18194daeb2d6"
        )

    def test_parse_uuid_object(self):
        _uuid = uuid.UUID("c4da8450-ec7a-4d3b-9ade-18194daeb2d6")
        assert UUID.parse(_uuid) == _uuid

    def test_serialize(self):
        assert (
            UUID.serialize(uuid.UUID("c4da8450-ec7a-4d3b-9ade-18194daeb2d6"))
            == "c4da8450-ec7a-4d3b-9ade-18194daeb2d6"
        )

    def test_parse_invalid(self):
        with pytest.raises(ScalarParsingError) as exc_info:
            UUID.parse("foo")
        assert str(exc_info.value) == "badly formed hexadecimal UUID string"

    def test_serialize_invalid(self):
        with pytest.raises(ScalarSerializationError) as exc_info:
            UUID.serialize("foo")
        assert str(exc_info.value) == "badly formed hexadecimal UUID string"


class TestRegexType(object):
    def test_accepts_string(self):
        t = RegexType("RE", r"[a-z][a-z_]*")
        assert t.parse("a_b") == "a_b"

    def test_accepts_compiled_regex(self):
        p = re.compile(r"[a-d]+", re.IGNORECASE)
        t = RegexType("RE", p)
        assert t.parse("aD") == "aD"

    def test_parse_fail(self):
        p = re.compile(r"^[a-d]+$", re.IGNORECASE)
        t = RegexType("RE", p)
        with pytest.raises(ScalarParsingError) as exc_info:
            t.parse("aF")
        assert str(exc_info.value) == '"aF" does not match pattern "^[a-d]+$"'

    def test_parse_literal_ok(self):
        p = re.compile(r"^[a-d]+$", re.IGNORECASE)
        t = RegexType("RE", p)
        assert t.parse_literal(parse_value('"aBcD"')) == "aBcD"

    def test_parse_literal_fail(self):
        p = re.compile(r"^[a-d]+$", re.IGNORECASE)
        t = RegexType("RE", p)
        with pytest.raises(ScalarParsingError) as exc_info:
            t.parse_literal(parse_value('"aF"'))
        assert str(exc_info.value) == '"aF" does not match pattern "^[a-d]+$"'

    def test_parse_literal_non_string(self):
        p = re.compile(r"^[a-d]+$", re.IGNORECASE)
        t = RegexType("RE", p)
        with pytest.raises(ScalarParsingError) as exc_info:
            t.parse_literal(parse_value("1"))
        assert str(exc_info.value) == "Invalid literal IntValue"
