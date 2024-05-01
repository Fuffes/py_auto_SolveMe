from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "received status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "received number of items is not equal to expected"