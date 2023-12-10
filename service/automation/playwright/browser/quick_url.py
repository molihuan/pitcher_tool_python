from msilib.schema import tables
from os import path
import time
import pyotp
from playwright.sync_api import sync_playwright
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg
from service.utils.file_utils import FileUtils
from service.utils.playwright_utils import PlaywrightUtils


class QuickUrl():
    # 主页
    @staticmethod
    def openFacebookMainPage(browserId: str):
        debugConfig=PlaywrightUtils.getBrowserDebugConfigMsg(browserId=browserId)

        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context = contexts[0]
            page = context.new_page()
            page.goto('https://www.facebook.com/')
    # 授权页面
    @staticmethod
    def openFacebookProfileAccess(browserId: str):
        debugConfig=PlaywrightUtils.getBrowserDebugConfigMsg(browserId=browserId)

        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context = contexts[0]
            page = context.new_page()
            page.goto('https://www.facebook.com/settings/?tab=profile_access')
    # 业务支持中心
    @staticmethod
    def openFacebookBusinessSupportHome(browserId: str):
        debugConfig=PlaywrightUtils.getBrowserDebugConfigMsg(browserId=browserId)
        time.sleep(1.2)
        facebookMsg=PlaywrightUtils.getFacebookAccountMsg(browserId=browserId)

        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context = contexts[0]
            page = context.new_page()
            #需要facebook账号
            #https://www.facebook.com/business-support-home/100058994730482/
            page.goto('https://www.facebook.com/business-support-home/'+facebookMsg.userName)
    # 广告账户BM
    @staticmethod
    def openFacebookAdAccounts(browserId: str):
        debugConfig=PlaywrightUtils.getBrowserDebugConfigMsg(browserId=browserId)

        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context = contexts[0]
            page = context.new_page()
            #需要企业id
            #https://business.facebook.com/settings/ad-accounts?business_id=349313897624365
            page.goto('https://business.facebook.com/settings/ad-accounts')
    # 聊天
    @staticmethod
    def openFacebookChatInbox(browserId: str):
        debugConfig=PlaywrightUtils.getBrowserDebugConfigMsg(browserId=browserId)

        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context = contexts[0]
            page = context.new_page()
            page.goto('https://business.facebook.com/latest/inbox')
    # 下户平台
    @staticmethod
    def openCyberklick(browserId: str):
        debugConfig=PlaywrightUtils.getBrowserDebugConfigMsg(browserId=browserId)

        with sync_playwright() as playwright:
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context = contexts[0]
            page = context.new_page()
            page.goto('https://business.cyberklick.com.cn/')
            