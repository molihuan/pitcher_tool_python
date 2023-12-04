from msilib.schema import tables
import time
import pyotp
from playwright.sync_api import sync_playwright
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg

class LogonConsumeReport():
    @staticmethod
    def run():
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("http://www.cnhfrj.top/base/data/dcdata")
            # 等待账号密码出现
            page.wait_for_selector('.login-code-img').screenshot(path="screenshot.png")