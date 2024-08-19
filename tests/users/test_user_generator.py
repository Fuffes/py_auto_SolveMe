import pytest
from src.generators.local_gen import LocalGen

@pytest.mark.parametrize("status", [
    '1',
    '2',
    '3',
])
def test_some1(status, get_user_generator):
    """test user generator"""
    user = get_user_generator.set_status(status).build()


def test_some2(get_user_generator):
    """test user generator with updating inner value"""
    to_send = get_user_generator.update_inner_value("local", LocalGen("en_US").build()).build()
    print(to_send)

@pytest.mark.parametrize(
    "localizations, abbr", [
        ('fr', "fr-FR"),
        ("en", "en-US"),
        ("de", "de-DE"),
    ]
)
def test_some3(localizations, abbr, get_user_generator):
    """test user generator with updating inner value"""
    to_send = get_user_generator.update_inner_value(["local", localizations], LocalGen(abbr).build()).build()
    print(to_send)
