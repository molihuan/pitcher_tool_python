import re

from service.models.facebook_account_msg import FacebookAccountMsg


class StrUtils():

    @staticmethod
    def has_whitespace(text: str) -> bool:
        return any(char.isspace() for char in text)
    
    @staticmethod
    def getFacebookAccountMsg(msg: str) -> FacebookAccountMsg:
        print(msg)
        # 处理回车键空格等
        msg = re.sub(r"\s+", "", msg)

        msg_list = msg.split('|')
        if len(msg_list) < 5:
            print("解析可能有误")
        id_card_img_url = msg_list[-2] if msg_list[-1] == "" else msg_list[-1]
        fm = FacebookAccountMsg(
            userName=msg_list[0],
            userPwd=msg_list[1],
            checkCode=msg_list[2],
            email=msg_list[3],
            emailPwd=msg_list[4],
            idCardImgUrl=id_card_img_url,
        )
        return fm

    @staticmethod
    def getBlackFacebookAccountMsg(msg: str) -> FacebookAccountMsg:
        print(msg)
        # 处理前后空格
        msg = msg.strip()
        msg_list = msg.split('\t')
        if len(msg_list) < 3:
            print("解析可能有误")

        fm = FacebookAccountMsg(
            userName=msg_list[0],
            userPwd=msg_list[1],
            cookie=msg_list[2]
        )
        return fm

    @staticmethod
    def getFacebookAccountMsgByRemark(msg: str) -> FacebookAccountMsg:
        print(msg)

        msg_list = msg.split('\n')
        if len(msg_list) < 4:
            print("备注信息不完整")
            return None

        # id_card_img_url = msg_list[-2] if msg_list[-1] == "" else msg_list[-1]
        fm = FacebookAccountMsg(
            checkCode=msg_list[0],
            email=msg_list[1],
            emailPwd=msg_list[2],
            idCardImgUrl=msg_list[3],
        )
        return fm
