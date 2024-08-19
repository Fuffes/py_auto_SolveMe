from faker import Faker
from src.base_class.base_builder import Builer


class LocalGen(Builer):

    def __init__(self, lang):
        super().__init__()
        self.faker = Faker(lang)
        self.result = {
            "name": self.faker.name()
        }


