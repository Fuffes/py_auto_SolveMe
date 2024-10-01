from src.generators.local_gen import LocalGen
from src.base_class.base_builder import Builer


class UserGen(Builer):

    def __init__(self):
        super().__init__()
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
            }
        return self







