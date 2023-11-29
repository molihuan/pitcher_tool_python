import json


class GroupMsg():
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data):
        data_dict = json.loads(json_data)
        return cls(**data_dict)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
