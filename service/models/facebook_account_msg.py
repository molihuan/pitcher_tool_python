class FacebookAccountMsg:
    def __init__(self, userName, userPwd, checkCode, email, emailPwd, idCardImgUrl):
        self.userName = userName
        self.userPwd = userPwd
        self.checkCode = checkCode
        self.email = email
        self.emailPwd = emailPwd
        self.idCardImgUrl = idCardImgUrl

    def __str__(self):
        return f"User Name: {self.userName}, User Password: {self.userPwd}, Check Code: {self.checkCode}, Email: {self.email}, Email Password: {self.emailPwd}, ID Card Image URL: {self.idCardImgUrl}"
