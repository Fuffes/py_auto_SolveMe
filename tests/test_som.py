from configuration import BASE_URL
from src.enums.global_enums import GlobalErrorMessages as error
import requests
import json

def test_getting_posts():
    respons = requests.get(url="https://restful-booker.herokuapp.com/booking/1")
    data = respons.json()

    assert respons.status_code == 200, error.WRONG_STATUS_CODE.value
    assert len(data) == 6, error.WRONG_ELEMENT_COUNT
