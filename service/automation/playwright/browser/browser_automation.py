from msilib.schema import tables
from os import path
import time
import pyotp
from playwright.sync_api import sync_playwright
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg
from service.utils.file_utils import FileUtils
from service.utils.playwright_utils import PlaywrightUtils


class BrowserAutomation():
    @staticmethod
    def loginOutlook(browserId: str):
        debugConfig=PlaywrightUtils.getBrowserDebugConfigMsg(browserId=browserId)
        time.sleep(1.2)
        facebookMsg=PlaywrightUtils.getFacebookAccountMsg(browserId=browserId)

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

            try:
                # 进入登录页
                page.wait_for_selector('a[data-bi-cn="SignIn"]',timeout=10000).first.click()
                page.wait_for_timeout(2000)
                page.close()
                page = context.pages[-1]
            except:
                print('没有检测到登录按钮')
                pass
            
            page.wait_for_timeout(1000)

            try:
                # 输入账号
                page.wait_for_selector('//*[@id="i0116"]',timeout=10000).fill(facebookMsg.email)
                page.locator('//*[@id="idSIButton9"]').click()
                print('没有检测到输入账号')
            except:
                pass

            
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
                try:
                    # 保持登录状态?
                    page.wait_for_selector('//*[@id="idSIButton9"]',timeout=10000).click()
                except:
                    print('没有保持登录状态?选项')
                    pass
                
                
            page.wait_for_timeout(1000)
            try:
                # 摆脱密码束缚
                page.wait_for_selector('//*[@id="iCancel"]').click()
            except:
                pass
    @staticmethod
    def input2fa(browserId: str):
        debugConfig=PlaywrightUtils.getBrowserDebugConfigMsg(browserId=browserId)
        time.sleep(1.2)
        facebookMsg=PlaywrightUtils.getFacebookAccountMsg(browserId=browserId)

        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            # 获取当前已打开的所有上下文
            contexts = browser.contexts
            context = contexts[0]
            pages = context.pages
            targetPage = None
            for page in pages:
                chooseOne=page.url.startswith('https://business.facebook.com/security/twofactor/reauth')
                if chooseOne:
                    targetPage = page
                    break
            if targetPage == None:
                print('不需要输入2fa')
                return
            # 输入二次验证码
            totp = pyotp.TOTP(facebookMsg.checkCode)
            print(totp.now())
            targetPage.wait_for_selector('//*[@id="js_2"]').fill(totp.now())
            targetPage.get_by_role('button').last.click()
            # targetPage.reload()



            