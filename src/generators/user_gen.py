from src.generators.local_gen import LocalGen

class UserGen():

    def __init__(self):
        self.result = {}
        self.reset()


    def set_status(self, status="-"):
        self.result["status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="-"):
        self.result["avatar"] = avatar
        return self

    def reset(self):
        self.set_balance()
        self.set_status()
        self.set_avatar()
        self.result["local"] = {
                "en": LocalGen("en_US").build(),
                "ru": LocalGen("ru_RU").build()
            }
        return self


    def update_inner_generator(self, key, value):
        self.result[key] = {value.build()}

    def build(self):
        return self.result



