from ..enums.global_enums import GlobalErrorMessages as error


class Response():

    def __init__(self, resp):
        self.response = resp
        self.response_json = resp.json()
        self.response_status_code = resp.status_code

    #shema
    # def validate(self, schema):
    #     if isinstance(self.response_json, list):
    #         for item in self.response_json:
    #             validate(item, schema)
    #     else: validate(self.response_json, schema)

    #PYDANTIC
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema(**item)
        else: schema(**self.response_json)


    def assert_status_code(self, exp_status_code):
        if isinstance(exp_status_code, list):
            for status in exp_status_code:
                assert self.response_status_code == status, error.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == exp_status_code, error.WRONG_STATUS_CODE.value
        return self