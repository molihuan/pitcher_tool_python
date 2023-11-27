from service.models.facebook_account_msg import FacebookAccountMsg


class StrUtils():
    @staticmethod
    def getFacebookAccountMsg(msg: str) -> FacebookAccountMsg:
        # 处理回车键
        msg = msg.replace('\n', '')

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
