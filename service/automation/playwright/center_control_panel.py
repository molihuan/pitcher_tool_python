import json
from msilib.schema import tables
from os import path
import time
import pyotp
from playwright.sync_api import sync_playwright
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg
from service.utils.file_utils import FileUtils


# 打开中控面板
class CenterControlPanel():
    @staticmethod
    def run(facebookMsg: FacebookAccountMsg | None, debugConfig: BrowserDebugConfig):
        with sync_playwright() as playwright:
            indexPath = path.join(FileUtils.getClientPath(), 'index.html')
            # 调试地址
            browser = playwright.chromium.connect_over_cdp(endpoint_url=debugConfig.debugWsUrl)
            contexts = browser.contexts
            context = contexts[0]
            page = context.new_page()
            page.goto('file:///' + indexPath)
            page.wait_for_timeout(1500)
            # 获取所有页面（标签页）的列表
            pages = context.pages
            # 切换到最后一个标签页
            page = pages[-1]
            saveObj = {
                "browserId": debugConfig.browserId,
                "facebookMsg": facebookMsg.to_dict()
            }

            # 设置LocalStorage浏览器id
            page.evaluate(f'localStorage.setItem("browserDebugConfig", JSON.stringify({saveObj}))')

            # 刷新页面以使修改生效
            page.reload()

            print(page.title())
