

class Builer():

    def __init__(self):
        self.result = {}

    def update_inner_value(self, entered_keys, value):
        if not isinstance(entered_keys, list):
            self.result[entered_keys] = value
        else:
            temp = self.result
            for item in entered_keys[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[entered_keys[-1]] = value
        return self

    def build(self):
        return self.result
