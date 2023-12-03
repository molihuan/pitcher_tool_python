class FacebookAccountMsg:
    def __init__(self, userName=None, userPwd=None, checkCode=None, email=None, emailPwd=None, idCardImgUrl=None):
        self.userName = userName
        self.userPwd = userPwd
        self.checkCode = checkCode
        self.email = email
        self.emailPwd = emailPwd
        self.idCardImgUrl = idCardImgUrl

    def __str__(self):
        return f"User Name: {self.userName}, User Password: {self.userPwd}, Check Code: {self.checkCode}, Email: {self.email}, Email Password: {self.emailPwd}, ID Card Image URL: {self.idCardImgUrl}"
