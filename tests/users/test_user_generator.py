import pytest

@pytest.mark.parametrize("status", [
    '1',
    '2',
    '3',
])
def test_some1(status, get_user_generator):
    """test user generator"""
    user = get_user_generator.set_status(status).build()
    print(user)