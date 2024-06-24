from pydantic import BaseModel, validate_call
from datetime import date


class BookingDates(BaseModel):
    checkin: date
    checkout: date


class Booking(BaseModel):
    firstname : str
    lastname : str
    totalprice : float
    depositpaid : bool
    bookingdates : BookingDates
    additionalneeds : str


class BookingList(BaseModel):
    bookingid : int
#
#     @validate_call("id")
#     def id_less_than_two(cls, v):
#         if v > 2:
#             raise ValueError("Id is not less than two")
#         else:
#             return v
