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
class LogonOutlook():
    @staticmethod
    def run(facebookMsg:FacebookAccountMsg,debugConfig:BrowserDebugConfig):
        options = webdriver.ChromeOptions()
        # 调试地址
        options.add_experimental_option("debuggerAddress",debugConfig.debugUrl)
        # 设置驱动位置
        service = Service(executable_path=debugConfig.webDriver)
        driver = webdriver.Chrome(service=service, options=options)
        ####################################################

        driver.switch_to.new_window(WindowTypes.TAB)
        driver.get("https://outlook.com/")
        driver.switch_to.window(driver.window_handles[-1])

        SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'a[data-bi-cn="SignIn"]')).click()

        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(1)

        try:
            # 输入账号
            SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="i0116"]')).send_keys(facebookMsg.email)
            driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
            time.sleep(1)
            # 输入密码
            SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="i0118"]')).send_keys(facebookMsg.emailPwd)
            driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
        except:
            # driver.get("https://outlook.com/")
            pass



        try:
            # 我们即将更新条款
            SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="iNext"]'),timeout=4).click()
        except:

            pass

        try:
            # 辅助邮箱
            SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="iShowSkip"]'),timeout=3).click()
        except:

            pass

        time.sleep(1)

        try:
            # 保持登录状态
            SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="acceptButton"]'),timeout=2).click()
        except:
            # 保持登录状态
            SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="idSIButton9"]'),timeout=3).click()
            pass

        time.sleep(1)

        try:
            # 摆脱密码束缚
            driver.find_element(By.XPATH,'//*[@id="iCancel"]').click()
        except:
            pass

