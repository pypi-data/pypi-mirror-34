# -*- coding: utf-8 -*-
""" ported from graphql-js """

import pytest
from py_gql._string_utils import parse_block_string, wrapped_lines, levenshtein


def test_parse_block_string_removes_uniform_indentation_from_a_string():
    raw_value = "\n".join(
        ["", "    Hello,", "      World!", "", "    Yours,", "      GraphQL."]
    )
    assert parse_block_string(raw_value) == "\n".join(
        ["Hello,", "  World!", "", "Yours,", "  GraphQL."]
    )


def test_parse_block_string_removes_empty_leading_and_trailing_lines():
    raw_value = "\n".join(
        [
            "",
            "",
            "    Hello,",
            "      World!",
            "",
            "    Yours,",
            "      GraphQL.",
            "",
            "",
        ]
    )

    assert parse_block_string(raw_value) == "\n".join(
        ["Hello,", "  World!", "", "Yours,", "  GraphQL."]
    )


def test_parse_block_string_removes_blank_leading_and_trailing_lines():
    raw_value = "\n".join(
        [
            "  ",
            "        ",
            "    Hello,",
            "      World!",
            "",
            "    Yours,",
            "      GraphQL.",
            "        ",
            "  ",
        ]
    )

    assert parse_block_string(raw_value) == "\n".join(
        ["Hello,", "  World!", "", "Yours,", "  GraphQL."]
    )


def test_parse_block_string_retains_indentation_from_first_line():
    raw_value = "\n".join(
        ["    Hello,", "      World!", "", "    Yours,", "      GraphQL."]
    )

    assert parse_block_string(raw_value) == "\n".join(
        ["    Hello,", "  World!", "", "Yours,", "  GraphQL."]
    )


def test_parse_block_string_does_not_alter_trailing_spaces():
    raw_value = "\n".join(
        [
            "               ",
            "    Hello,     ",
            "      World!   ",
            "               ",
            "    Yours,     ",
            "      GraphQL. ",
            "               ",
        ]
    )

    assert parse_block_string(raw_value) == "\n".join(
        [
            "Hello,     ",
            "  World!   ",
            "           ",
            "Yours,     ",
            "  GraphQL. ",
        ]
    )


def test_wrapped_lines():
    source_lines = [
        "This line is shorter and should not be wrapped.",
        "This line is long and should be wrapped at around this position.",
        "This line is longer and should be wrapped twice. This line is longer and "
        "should be wrapped twice.",
        "It should also wrap around underscores like this_token",
        "and it should also wrap around dashes like this-kind-of-token.",
    ]

    assert list(wrapped_lines(source_lines, 50)) == [
        "This line is shorter and should not be wrapped.",
        "This line is long and should be wrapped at around ",
        "this position.",
        "This line is longer and should be wrapped twice. ",
        "This line is longer and should be wrapped twice.",
        "It should also wrap around underscores like this_",
        "token",
        "and it should also wrap around dashes like this-",
        "kind-of-token.",
    ]


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("", "", 0),
        ("a", "", 1),
        ("", "a", 1),
        ("abc", "", 3),
        ("", "abc", 3),
        ("", "", 0),
        ("a", "a", 0),
        ("abc", "abc", 0),
        ("", "a", 1),
        ("a", "ab", 1),
        ("b", "ab", 1),
        ("ac", "abc", 1),
        ("abcdefg", "xabxcdxxefxgx", 6),
        ("a", "", 1),
        ("ab", "a", 1),
        ("ab", "b", 1),
        ("abc", "ac", 1),
        ("xabxcdxxefxgx", "abcdefg", 6),
        ("a", "b", 1),
        ("ab", "ac", 1),
        ("ac", "bc", 1),
        ("abc", "axc", 1),
        ("xabxcdxxefxgx", "1ab2cd34ef5g6", 6),
        ("example", "samples", 3),
        ("sturgeon", "urgently", 6),
        ("levenshtein", "frankenstein", 6),
        ("distance", "difference", 5),
        ("java was neat", "scala is great", 7),
    ],
)
def test_levenshtein(a, b, expected):
    assert levenshtein(a, b) == expected
