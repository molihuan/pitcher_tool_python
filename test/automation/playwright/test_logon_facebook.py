import email
import sys
import time
from urllib import response
import pyotp
from playwright.sync_api import sync_playwright

sys.path.append('E:\\software\\python\\Project\\pitcher_tool_python')

from service.utils.str_utils import StrUtils
from service.models.browser_debug_config import BrowserDebugConfig
from service.http.http import HttpUtils

from service.models.facebook_account_msg import FacebookAccountMsg

user_id = 'jccmbhf'

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
    page=context.new_page()
    page.goto("https://facebook.com")
    page.wait_for_timeout(2000)
    # 切换到最后一个标签页
    page = context.pages[-1]

    # 等待账号密码出现
    email_input = page.wait_for_selector('input[id="email"]')
    pd_email = email_input.input_value()
    while (pd_email == None) or (pd_email == ''):
        time.sleep(1)
        pd_email = email_input.input_value()

    print(pd_email)

    # 点击登录按钮
    page.locator('button[name="login"]').click()
    # 输入二次验证码
    totp = pyotp.TOTP(facebookMsg.checkCode)
    print(totp.now())
    page.locator('input[class="inputtext"]').fill(totp.now())
    page.locator('button[value="continue"]').click()

    # 继续
    page.locator('button[value="Continue"]').click()

    # 正常的话已经进入了
    try:
        # 有验证
        # print("需要获取邮箱验证码")
        # SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=4).click()
        # SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=3).click()
        # SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=3).click()
        pass
    except:

        pass
