from ..enums.global_enums import GlobalErrorMessages as error


class Response():
    # TODO check problem with   self.response_data = self.response_json.get("data")
    def __init__(self, resp):
        self.response = resp
        self.response_json = resp.json()
        # self.response_data = self.response_json.get("data")
        self.response_status_code = resp.status_code

    #shema
    # def validate(self, schema):
    #     if isinstance(self.response_json, list):
    #         for item in self.response_json:
    #             validate(item, schema)
    #     else: validate(self.response_json, schema)

    # TODO modify validate method to work with "data"
    #PYDANTIC
    def validate(self, schema):
        if isinstance(self.response_json.get("data"), list):
            for item in self.response_json.get("data"):
                schema(**item)
        else: schema(**self.response_json.get("data"))


    def assert_status_code(self, exp_status_code):
        if isinstance(exp_status_code, list):
            for status in exp_status_code:
                assert self.response_status_code == status, self
        else:
            assert self.response_status_code == exp_status_code, self
        return self


    def __str__(self):
        return (
                f"status code: {self.response_status_code} \n\
                req. url : {self.response.url}\n\ resp.body: {self.response_json}"
                )