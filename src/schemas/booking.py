BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "firstname": {
            "type": "string"
        },
        "lastname": {
            "type": "string"
        },
        "totalprice": {
            "type": "integer"
        },
        "depositpaid": {
            "type": "boolean"
        },
        "bookingdates": {
            "type": "object",
            "properties": {
                "checkin": {
                    "type": "string"
                },
                "checkout": {
                    "type": "string"
                }
            },
            "required": [
                "checkin",
                "checkout"
            ]
        },
        "additionalneeds": {
            "type": "string"
        }
    },
    "required": [
        "firstname",
        "lastname",
    ]
}


BOOKING_LIST_SCHEMA = {
    "type" : "object",
    "properties" : {
        "bookingid" : {"type" : "number"}

    }
}


#
# {'firstname': 'Susan',
#  'lastname': 'Brown',
#  'totalprice': 286,
#  'depositpaid': True,
#  'bookingdates': {'checkin': '2016-11-07', 'checkout': '2017-02-01'},
#  'additionalneeds': 'Breakfast'
#  }
