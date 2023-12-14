from msilib.schema import tables
from os import path
import time
import pyotp
import pyperclip
from playwright.sync_api import sync_playwright
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg
from service.utils.file_utils import FileUtils
from service.utils.playwright_utils import PlaywrightUtils


class QuickMsg():
    # 复制2fa
    @staticmethod
    def copy2fa(browserId: str):
        facebookMsg = PlaywrightUtils.getFacebookAccountMsg(browserId=browserId)
        totp = pyotp.TOTP(facebookMsg.checkCode)
        print(totp.now())
        pyperclip.copy(totp.now())
