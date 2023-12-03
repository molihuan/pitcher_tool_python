from msilib.schema import tables
import time
import pyotp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg
from service.utils.selenium_utils import SeleniumUtils
class LogonFacebook():
    @staticmethod
    def run(facebookMsg:FacebookAccountMsg,debugConfig:BrowserDebugConfig):
        options = webdriver.ChromeOptions()
        # 调试地址
        options.add_experimental_option("debuggerAddress",debugConfig.debugUrl)
        # 设置驱动位置
        service = Service(executable_path=debugConfig.webDriver)
        driver = webdriver.Chrome(service=service, options=options)
        driver.switch_to.new_window(WindowTypes.TAB)
        driver.get("https://facebook.com")
        driver.switch_to.window(driver.window_handles[-1])

        # 等待账号密码出现
        SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'input[id="email"]'))
        SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'input[id="pass"]'))

        # 点击登录按钮 
        SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[name="login"]')).click()

        # 输入二次验证码
        totp = pyotp.TOTP(facebookMsg.checkCode)
        print(totp.now())
        SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'input[class="inputtext"]')).send_keys(totp.now())
        SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="continue"]')).click()
        #继续
        SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]')).click()
        #正常的话已经进入了
        try:
            #有验证
            print("需要获取邮箱验证码")
            # SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=4).click()
            # SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=3).click()
            # SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=3).click()
            pass
        except:

            pass


