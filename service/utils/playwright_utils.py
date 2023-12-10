from service.http.http import HttpUtils
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg
from service.utils.str_utils import StrUtils


class PlaywrightUtils():
    @staticmethod
    def getFacebookAccountMsg(browserId: str) -> FacebookAccountMsg:
        print(browserId)

        # 获取账户是否打开状态
        status = HttpUtils.startupStatus(browserId)

        print(status)

        if (status == None) or (status['code'] != 0) or (status['data']['status'] != "Active"):
            print("获取状态失败")

        # 获取用户信息
        accountResp = HttpUtils.getAccounts(user_id=browserId, page=1)
        if (status == None) or (status['code'] != 0):
            print("用户信息获取失败")
        firstAccount = accountResp['data']['list'][0]
        print(firstAccount)

        facebookMsg = StrUtils.getFacebookAccountMsgByRemark(firstAccount['remark'])
        facebookMsg.userName = firstAccount['username']
        facebookMsg.userPwd = firstAccount['password']

        return facebookMsg
    
    @staticmethod
    def getBrowserDebugConfigMsg(browserId: str)->BrowserDebugConfig :
        print(browserId)

        # 获取账户是否打开状态
        status = HttpUtils.startupStatus(browserId)

        print(status)

        if (status == None) or (status['code'] != 0) or (status['data']['status'] != "Active"):
            print("获取状态失败")

        # 获取调试地址
        debugWsUrl = status['data']['ws']['puppeteer']
        debugConfig = BrowserDebugConfig(debugWsUrl=debugWsUrl,browserId=browserId)
        return debugConfig