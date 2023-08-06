# -*- coding: utf-8 -*-

import pytest

from py_gql.execution import execute
from py_gql.lang import parse


def test_it_correctly_identifies_r2_d2_as_the_hero_of_the_star_wars_saga(
    starwars_schema
):
    result, errors = execute(
        starwars_schema,
        parse(
            """
            query HeroNameQuery {
                hero {
                name
                }
            }
            """
        ),
    ).result()
    assert result == {"hero": {"name": "R2-D2"}}
    assert errors == []


def test_id_and_friends_of_r2_d2(starwars_schema):
    result, errors = execute(
        starwars_schema,
        parse(
            """
            query HeroNameAndFriendsQuery {
                hero {
                    id
                    name
                    friends {
                        name
                    }
                }
            }
            """
        ),
    ).result()
    assert result == {
        "hero": {
            "id": "2001",
            "name": "R2-D2",
            "friends": [
                {"name": "Luke Skywalker"},
                {"name": "Han Solo"},
                {"name": "Leia Organa"},
            ],
        }
    }
    assert errors == []


def test_the_friends_of_friends_of_r2_d2(starwars_schema):
    result, errors = execute(
        starwars_schema,
        parse(
            """
            query NestedQuery {
                hero {
                    name
                    friends {
                        name
                        appearsIn
                        friends {
                        name
                        }
                    }
                }
            }
            """
        ),
    ).result()
    assert result == {
        "hero": {
            "name": "R2-D2",
            "friends": [
                {
                    "name": "Luke Skywalker",
                    "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"],
                    "friends": [
                        {"name": "Han Solo"},
                        {"name": "Leia Organa"},
                        {"name": "C-3PO"},
                        {"name": "R2-D2"},
                    ],
                },
                {
                    "name": "Han Solo",
                    "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"],
                    "friends": [
                        {"name": "Luke Skywalker"},
                        {"name": "Leia Organa"},
                        {"name": "R2-D2"},
                    ],
                },
                {
                    "name": "Leia Organa",
                    "appearsIn": ["NEWHOPE", "EMPIRE", "JEDI"],
                    "friends": [
                        {"name": "Luke Skywalker"},
                        {"name": "Han Solo"},
                        {"name": "C-3PO"},
                        {"name": "R2-D2"},
                    ],
                },
            ],
        }
    }
    assert errors == []


def test_luke_skywalker_using_id(starwars_schema):
    result, errors = execute(
        starwars_schema,
        parse(
            """
            query FetchLukeQuery {
                human(id: "1000") {
                name
                }
            }
            """
        ),
    ).result()
    assert result == {"human": {"name": "Luke Skywalker"}}
    assert errors == []


@pytest.mark.parametrize(
    "id_, expected",
    [
        ("1000", {"name": "Luke Skywalker"}),
        ("1002", {"name": "Han Solo"}),
        ("not a valid id", None),
    ],
)
def test_generic_query_using_id_and_variable(starwars_schema, id_, expected):
    result, errors = execute(
        starwars_schema,
        parse(
            """
            query FetchSomeIDQuery($someId: String!) {
                human(id: $someId) {
                name
                }
            }
            """
        ),
        variables={"someId": id_},
    ).result()
    assert result == {"human": expected}
    assert errors == []


def test_changing_key_with_alias(starwars_schema):
    result, errors = execute(
        starwars_schema,
        parse(
            """
            query FetchLukeAliased {
                luke: human(id: "1000") {
                name
                }
            }
            """
        ),
    ).result()
    assert result == {"luke": {"name": "Luke Skywalker"}}
    assert errors == []


def test_same_root_field_multiple_aliases(starwars_schema):
    result, errors = execute(
        starwars_schema,
        parse(
            """
            query FetchLukeAndLeiaAliased {
                luke: human(id: "1000") {
                    name
                    homePlanet
                }
                leia: human(id: "1003") {
                    name
                    homePlanet
                }
            }
            """
        ),
    ).result()
    assert result == {
        "luke": {"name": "Luke Skywalker", "homePlanet": "Tatooine"},
        "leia": {"name": "Leia Organa", "homePlanet": "Alderaan"},
    }
    assert errors == []


def test_use_of_fragment_to_avoid_duplicate_content(starwars_schema):
    result, errors = execute(
        starwars_schema,
        parse(
            """
            query FetchLukeAndLeiaAliased {
                luke: human(id: "1000") { ...HumanFragment }
                leia: human(id: "1003") { ...HumanFragment }
            }

            fragment HumanFragment on Human { name homePlanet }
            """
        ),
    ).result()
    assert result == {
        "luke": {"name": "Luke Skywalker", "homePlanet": "Tatooine"},
        "leia": {"name": "Leia Organa", "homePlanet": "Alderaan"},
    }
    assert errors == []


@pytest.mark.parametrize(
    "query, result",
    [
        (
            "query CheckTypeOfR2 { hero { __typename name } }",
            {"hero": {"__typename": "Droid", "name": "R2-D2"}},
        ),
        (
            "query CheckTypeOfLuke { hero(episode: EMPIRE) { __typename name } }",
            {"hero": {"__typename": "Human", "name": "Luke Skywalker"}},
        ),
    ],
)
def test_introspection(starwars_schema, query, result):
    data, errors = execute(starwars_schema, parse(query)).result()
    assert data, errors == (result, [])


def test_error_on_accessing_secret_backstory(starwars_schema):
    data, errors = execute(
        starwars_schema,
        parse(
            """
            query HeroNameQuery {
                hero {
                    name
                    secretBackstory
                }
            }
            """
        ),
    ).result()
    assert data == {"hero": {"name": "R2-D2", "secretBackstory": None}}
    assert len(errors) == 1
    err = errors[0]
    assert str(err) == "secretBackstory is secret."
    assert err.path == ["hero", "secretBackstory"]
    assert err.nodes[0].loc == (103, 118)


def test_error_on_accessing_secret_backstory_in_a_list(starwars_schema):
    data, errors = execute(
        starwars_schema,
        parse(
            """
            query HeroNameQuery {
                hero {
                    name
                    friends {
                        name
                        secretBackstory
                    }
                }
            }
            """
        ),
    ).result()
    assert data == {
        "hero": {
            "friends": [
                {"name": "Luke Skywalker", "secretBackstory": None},
                {"name": "Han Solo", "secretBackstory": None},
                {"name": "Leia Organa", "secretBackstory": None},
            ],
            "name": "R2-D2",
        }
    }
    assert len(errors) == 3
    for i, err in enumerate(errors):
        assert str(err) == "secretBackstory is secret."
        assert err.path == ["hero", "friends", i, "secretBackstory"]
        assert err.nodes[0].loc == (166, 181)


def test_error_on_accessing_secret_backstory_through_alias(starwars_schema):
    data, errors = execute(
        starwars_schema,
        parse(
            """
            query HeroNameQuery {
                mainHero: hero {
                    name
                    story: secretBackstory
                }
            }
            """
        ),
    ).result()
    assert data == {"mainHero": {"name": "R2-D2", "story": None}}
    assert len(errors) == 1
    err = errors[0]
    assert str(err) == "secretBackstory is secret."
    assert err.path == ["mainHero", "story"]
    assert err.nodes[0].loc == (113, 135)


def test_error_on_missing_argument(starwars_schema):
    data, errors = execute(
        starwars_schema,
        parse(
            """
            {
                luke: human {
                    name
                }
            }
            """
        ),
    ).result()
    assert data == {"luke": None}
    assert len(errors) == 1
    err = errors[0]
    assert (
        str(err) == 'Argument "id" of required type "String!" was not provided'
    )
    assert err.path == ["luke"]
