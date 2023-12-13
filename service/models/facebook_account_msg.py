import json


class FacebookAccountMsg:
    def __init__(self, userName: str = None, userPwd: str = None, checkCode=None, email=None, emailPwd=None,
                 idCardImgUrl=None,
                 cookie=None):
        self.userName = userName
        self.userPwd = userPwd
        self.checkCode = checkCode
        self.email = email
        self.emailPwd = emailPwd
        self.idCardImgUrl = idCardImgUrl
        self.cookie = cookie
        
    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data):
        data_dict = json.loads(json_data)
        return cls(**data_dict)
    
    def to_dict(self):
        data_dict = {}
        for key, value in self.__dict__.items():
            if value is not None:
                data_dict[key] = value
        return data_dict
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def __str__(self):
        return f"User Name: {self.userName}, User Password: {self.userPwd}, Check Code: {self.checkCode}, Email: {self.email}, Email Password: {self.emailPwd}, ID Card Image URL: {self.idCardImgUrl}, cookie: {self.cookie}"
