from msilib.schema import tables
import time
import pyotp
from playwright.sync_api import sync_playwright
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg


class LogonFacebook():
    @staticmethod
    def run(facebookMsg: FacebookAccountMsg, debugConfig: BrowserDebugConfig):
        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context = contexts[0]
            page = context.new_page()
            page.goto("https://facebook.com")
            page.wait_for_timeout(1600)
            page = context.pages[-1]
            # 等待账号密码出现
            page.wait_for_selector('input[id="email"]')
            page.wait_for_selector('input[id="pass"]')
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
