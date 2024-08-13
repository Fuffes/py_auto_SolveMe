from faker import Faker

class LocalGen():
    def __init__(self, lang):
        self.faker = Faker(lang)
        self.result = {
            "name": self.faker.name()
        }

    def build(self):
        return self.result
