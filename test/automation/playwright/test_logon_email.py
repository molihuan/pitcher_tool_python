import sys
import time
from urllib import response
import pyotp
from playwright.sync_api import sync_playwright

sys.path.append('E:\\software\\python\\Project\\pitcher_tool_python')

from service.utils.str_utils import StrUtils
from service.models.browser_debug_config import BrowserDebugConfig
from service.http.http import HttpUtils

user_id = 'jc6yy6l'

# 获取账户是否打开状态
status = HttpUtils.startupStatus(user_id)

print(status)

if (status == None) or (status['code'] != 0) or (status['data']['status'] != "Active"):
    print("获取状态失败")

# 获取调试地址
debugWsUrl = status['data']['ws']['puppeteer']
debugConfig = BrowserDebugConfig(debugWsUrl=debugWsUrl)

# 获取用户信息
accountResp = HttpUtils.getAccounts(user_id=user_id, page=1)
if (status == None) or (status['code'] != 0):
    print("用户信息获取失败")
firstAccount = accountResp['data']['list'][0]
print(firstAccount)

facebookMsg = StrUtils.getFacebookAccountMsgByRemark(firstAccount['remark'])
facebookMsg.userName = firstAccount['username']
facebookMsg.userPwd = firstAccount['password']

with sync_playwright() as playwright:
    # 调试地址
    browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
    # 获取当前已打开的所有上下文
    contexts = browser.contexts
    context = contexts[0]
    page = context.new_page()
    page.goto("https://outlook.com/")
    page.wait_for_timeout(2000)
    # 切换到最后一个标签页
    page = context.pages[-1]
    # 进入登录页
    page.locator('a[data-bi-cn="SignIn"]').first.click()
    page.wait_for_timeout(2000)

    page = context.pages[-1]
    
    print(page.url)

    # 输入账号
    page.locator('//*[@id="i0116"]').fill(facebookMsg.email)
    page.locator('//*[@id="idSIButton9"]').click()

    # 输入密码
    page.locator('//*[@id="i0118"]').fill(facebookMsg.emailPwd)
    page.locator('//*[@id="idSIButton9"]').click()

    try:
        page.locator('//*[@id="iShowSkip"]').click(timeout=3)
    except:

        pass
    try:
        # 保持登录状态?
        page.locator('//*[@id="acceptButton"]').click(timeout=2)
    except:
        # 保持登录状态?
        page.locator('//*[@id="idSIButton9"]').click(timeout=3)
        pass

    try:
        # 摆脱密码束缚
        page.locator('//*[@id="iCancel"]').click()
    except:
        pass
