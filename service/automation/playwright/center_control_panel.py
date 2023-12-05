from msilib.schema import tables
from os import path
import time
import pyotp
from playwright.sync_api import sync_playwright
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg
from service.utils.file_utils import FileUtils


class CenterControlPanel():
    @staticmethod
    def run(facebookMsg: FacebookAccountMsg, debugConfig: BrowserDebugConfig):
        with sync_playwright() as playwright:
            indexPath = path.join(FileUtils.getClientPath(),'index.html')
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context=contexts[0]
            context.new_page().goto("file:///"+indexPath)
            # 获取所有页面（标签页）的列表
            pages = context.pages
            # 切换到最后一个标签页
            page = pages[-1]
