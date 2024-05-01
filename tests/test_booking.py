from configuration import BASE_URL
from src.enums.global_enums import GlobalErrorMessages as error
import requests
from jsonschema import validate
from src.schemas.booking import BOOKING_SCHEMA, BOOKING_LIST_SCHEMA
from src.base_class.response import Response
import json

def test_getting_booking_list():
    r = requests.get(url="https://restful-booker.herokuapp.com/booking/")
    data = Response(r)
    data.assert_status_code(200).validate(BOOKING_LIST_SCHEMA)
    print(r.json())

def test_getting_booking():
    r = requests.get(url="https://restful-booker.herokuapp.com/booking/1")
    data = Response(r)
    data.assert_status_code(200).validate(BOOKING_SCHEMA)
    print(r.json())
