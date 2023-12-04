import json


class ResponseBody():
    code: int
    data: object
    msg: str

    def __init__(self, code: int, data, msg: str):
        self.code = code
        self.data = data
        self.msg = msg

    def to_json(self):
        # 将字典转换为 JSON 字符串，并保留非 ASCII 字符
        return json.dumps(self.__dict__, ensure_ascii=False)

    @classmethod
    def success(cls, data, msg: str = '成功'):
        return cls(code=0, data=data, msg=msg)

    @classmethod
    def success_json(cls, data, msg: str = '成功'):
        return cls(code=0, data=data, msg=msg).to_json()

    @classmethod
    def success_json_encode(cls, data, msg: str = '成功'):
        return cls(code=0, data=data, msg=msg).to_json().encode('utf-8')

    @classmethod
    def error(cls, data, msg: str = '错误'):
        return cls(code=-1, data=data, msg=msg)

    @classmethod
    def error_json(cls, data, msg: str = '错误'):
        return cls(code=-1, data=data, msg=msg).to_json()

    @classmethod
    def error_json_encode(cls, data, msg: str = '错误'):
        return cls(code=-1, data=data, msg=msg).to_json().encode('utf-8')
