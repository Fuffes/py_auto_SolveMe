import pytest
import requests

from configuration import BASE_URL


@pytest.fixture
def get_users():
    response = requests.get(BASE_URL)
    return response