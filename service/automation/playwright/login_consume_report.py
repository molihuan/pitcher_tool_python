from msilib.schema import tables
import time
import pyotp
from flet_core import Page
from playwright.sync_api import sync_playwright

from service.dao.data_manager import DataManager
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg


class LogonConsumeReport():
    @staticmethod
    def run(page: Page):
        executable_path = DataManager.getBrowserPath(page)

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                executable_path=executable_path,
                headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("http://www.cnhfrj.top/base/data/dcdata")
            # 等待账号密码出现
            page.wait_for_selector('.login-code-img').screenshot(path="screenshot.png")
