import sys
import time
from urllib import response
import pyotp
from playwright.sync_api import sync_playwright

sys.path.append('E:\\software\\python\\Project\\pitcher_tool_python')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from service.utils.str_utils import StrUtils
from service.models.browser_debug_config import BrowserDebugConfig
from service.http.http import HttpUtils
from service.utils.selenium_utils import SeleniumUtils
from service.models.facebook_account_msg import FacebookAccountMsg

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
    context=contexts[0]
    context.new_page().goto("https://outlook.com/")
    # 切换到最后一个标签页
    page = context.pages[-1]
    # 进入登录页
    page.locator('a[data-bi-cn="SignIn"]').first.click()
    page.wait_for_timeout(2)
    print(len(context.pages))
    page = context.pages[-1]
    page.bring_to_front()

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
