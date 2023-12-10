from msilib.schema import tables
import time
import pyotp
from playwright.sync_api import sync_playwright
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg


class LoginOutlook():
    @staticmethod
    def run(facebookMsg: FacebookAccountMsg, debugConfig: BrowserDebugConfig):
        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            # 获取当前已打开的所有上下文
            contexts = browser.contexts
            context = contexts[0]
            # 启动跟踪功能
            page = context.new_page()
            page.goto("https://outlook.com/")
            page.wait_for_timeout(2000)
            # 切换到最后一个标签页
            page = context.pages[-1]
            # 进入登录页
            page.locator('a[data-bi-cn="SignIn"]').first.click()
            page.wait_for_timeout(2000)
            page.close()

            page = context.pages[-1]
            
            page.wait_for_timeout(1000)
            # 输入账号

            page.wait_for_selector('//*[@id="i0116"]').fill(facebookMsg.email)
            page.locator('//*[@id="idSIButton9"]').click()

            
            page.wait_for_timeout(1000)
            # 输入密码
            page.wait_for_selector('//*[@id="i0118"]').fill(facebookMsg.emailPwd)
            page.locator('//*[@id="idSIButton9"]').click()

            page.wait_for_timeout(1000)
            # 备用电子邮件
            try:
                page.wait_for_selector('//*[@id="iShowSkip"]',timeout=10000).click()
            except :
                print('没有出现备用邮箱选项')

            page.wait_for_timeout(1000)
            try:
                # 保持登录状态?
                page.wait_for_selector('//*[@id="acceptButton"]',timeout=10000).click()
            except :
                # 保持登录状态?
                page.wait_for_selector('//*[@id="idSIButton9"]',timeout=10000).click()
                print('没有保持登录状态?选项')
                
            page.wait_for_timeout(1000)
            try:
                # 摆脱密码束缚
                page.wait_for_selector('//*[@id="iCancel"]').click()
            except:
                pass