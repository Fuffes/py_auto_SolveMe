import pytest
import requests

from configuration import BASE_URL
from src.generators.user_gen import UserGen


@pytest.fixture
def get_users():
    response = requests.get(BASE_URL)
    return response


@pytest.fixture
def get_user_generator():
    return UserGen()