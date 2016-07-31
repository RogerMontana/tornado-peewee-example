import json


class Object:
    def convert_to_dict(self):
        return self.__dict__

    def convert_to_json(self):
        return json.dumps(self.convert_to_dict())
