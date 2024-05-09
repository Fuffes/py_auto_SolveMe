import requests
from src.schemas.booking import BOOKING_SCHEMA, BOOKING_LIST_SCHEMA
from src.base_class.response import Response
from src.pydantic_schemas.booking import Booking, BookingList


def test_getting_booking_list():
    r = requests.get(url="https://restful-booker.herokuapp.com/booking/")
    data = Response(r)
#     # schema
#     # data.assert_status_code(200).validate(BOOKING_LIST_SCHEMA)
#
#     # pydentic
    data.assert_status_code(200).validate(BookingList)


def test_getting_booking():
    r = requests.get(url="https://restful-booker.herokuapp.com/booking/1")
    data = Response(r)
    # #schema
    # # data.assert_status_code(200).validate(BOOKING_SCHEMA)
    # pydentic
    data.assert_status_code(200).validate(Booking)

