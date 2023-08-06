# -*- coding: utf-8 -*-
""" Test the main entry point """

import pytest
from py_gql.exc import SchemaError
from py_gql._graphql import graphql
from py_gql.schema import String, Schema


def test_it_correctly_identifies_r2_d2_as_the_hero_of_the_star_wars_saga(
    starwars_schema
):
    result = graphql(
        starwars_schema,
        """
        query HeroNameQuery {
            hero {
            name
            }
        }
        """,
    )
    assert result.response() == {"data": {"hero": {"name": "R2-D2"}}}


def test_correct_response_on_syntax_error_1(starwars_schema):
    assert graphql(starwars_schema, "", {}).response() == {
        "errors": [
            {
                "message": "Unexpected <EOF> (1:1):\n  1:\n    ^",
                "locations": [{"columne": 1, "line": 1}],
            }
        ]
    }


def test_correct_response_on_syntax_error_2(starwars_schema):
    query = """
    query HeroNameQuery {{
        hero {
           name
        }
    }
    """

    assert graphql(starwars_schema, query, {}).response() == {
        "errors": [
            {
                "message": """Expected Name but found "{" (2:26):
  1:
  2:    query HeroNameQuery {{
                             ^
  3:        hero {
  4:           name""",
                "locations": [{"columne": 26, "line": 2}],
            }
        ]
    }


def test_correct_response_on_validation_errors(starwars_schema):
    query = """
    query HeroNameAndFriendsQuery($hero: Droid) {
        hero {
            id
            foo
            friends {
                name
            }
        }
    }

    fragment hero on Character {
        id
        friends { name }
    }
    """
    assert graphql(starwars_schema, query, {}).response() == {
        "errors": [
            {
                "locations": [{"column": 35, "line": 2}],
                "message": 'Variable "$hero" must be input type',
            },
            {
                "locations": [{"column": 13, "line": 5}],
                "message": 'Cannot query field "foo" on type "Character"',
            },
            {"message": 'Unused fragment(s) "hero"'},
            {
                "locations": [{"column": 35, "line": 2}],
                "message": 'Unused variable "$hero"',
            },
        ]
    }


def test_correct_response_on_argument_validation_error(starwars_schema):
    query = """
    query HeroNameQuery {
        luke: human {
            name
        }
    }
    """
    assert graphql(starwars_schema, query, {}).response() == {
        "errors": [
            {
                "message": (
                    'Field "human" argument "id" of type String! '
                    "is required but not provided"
                ),
                "locations": [{"line": 3, "column": 9}],
            }
        ]
    }


def test_correct_response_on_execution_error(starwars_schema):
    query = """
    query HeroNameAndFriendsQuery {
        hero {
            id
            friends {
                name
            }
        }
    }

    query HeroNameQuery {
        hero {
           name
        }
    }
    """
    assert graphql(starwars_schema, query, {}).response() == {
        "errors": [
            {
                "message": "Operation name is required when document contains "
                "multiple operation definitions"
            }
        ],
        "data": None,
    }


def test_correct_response_on_execution_error_2(starwars_schema):
    query = """
    query HeroNameAndFriendsQuery {
        hero {
            id
            friends {
                name
            }
        }
    }

    query HeroNameQuery {
        hero {
           name
        }
    }
    """
    assert graphql(
        starwars_schema, query, {}, operation_name="Foo"
    ).response() == {
        "errors": [{"message": 'No operation "Foo" found in document'}],
        "data": None,
    }


def test_correct_response_on_execution_error_3(starwars_schema):
    query = """
    mutation  {
        hero {
            id
            friends {
                name
            }
        }
    }
    """
    assert graphql(starwars_schema, query, {}).response() == {
        "errors": [{"message": "Schema doesn't support mutation operation"}],
        "data": None,
    }


def test_correct_response_on_variables_error(starwars_schema):
    query = """
    query ($episode: Episode!, $human: String!) {
        hero(episode: $episode) {
            name
        }
        human(id: $human) {
            name
        }
    }
    """
    assert graphql(
        starwars_schema, query, {"episode": 42, "id": 42}
    ).response() == {
        "errors": [
            {
                "message": (
                    'Variable "$episode" got invalid value 42 '
                    "(Expected type Episode)"
                ),
                "locations": [{"line": 2, "column": 12}],
            },
            {
                "message": (
                    'Variable "$human" of required type "String!" '
                    "was not provided."
                ),
                "locations": [{"line": 2, "column": 32}],
            },
        ],
        "data": None,
    }


def test_correct_response_on_resolver_error(starwars_schema):
    query = """
    query HeroNameQuery {
        mainHero: hero {
            name
            story: secretBackstory
        }
    }
    """
    assert graphql(starwars_schema, query, {}).response() == {
        "errors": [
            {
                "message": "secretBackstory is secret.",
                "locations": [{"line": 5, "column": 13}],
                "path": ["mainHero", "story"],
                "extensions": {"code": 42},
            }
        ],
        "data": {"mainHero": {"name": "R2-D2", "story": None}},
    }


def test_raises_if_invalid_schema_is_provided():
    with pytest.raises(SchemaError) as exc_info:
        graphql(Schema(String), "{ field }", {})
    assert str(exc_info.value) == 'Query must be ObjectType but got "String"'
