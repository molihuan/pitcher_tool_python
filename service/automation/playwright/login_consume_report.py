import datetime
from os import path

from playwright.sync_api import sync_playwright

from service.utils.file_utils import FileUtils


# 登录消费报表
class LogonConsumeReport():
    @staticmethod
    def run():
        # executable_path = DataManager.getBrowserPath()
        executable_path = 'C:\\Users\\moli\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
        now = datetime.datetime.now()
        now_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        screenshotDirPath = path.join(FileUtils.getTempPath(), 'screenshot')
        screenshotPath = path.join(screenshotDirPath, f'{now_time}.png')

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                executable_path=executable_path,
                headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("http://www.cnhfrj.top/base/data/dcdata")
            page.wait_for_timeout(1500)
            page = context.pages[-1]
            # imgBytes = page.wait_for_selector('.login-code-img').screenshot(path=screenshotPath)
            # ocr = ddddocr.DdddOcr()
            # res = ocr.classification(imgBytes)
            # print(res)

            page.wait_for_timeout(5000)
