import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from service.models.browser_debug_config import BrowserDebugConfig
class LogonFacebook():
    @staticmethod
    def run(debugConfig:BrowserDebugConfig):
        options = webdriver.ChromeOptions()
        # 调试地址
        options.add_experimental_option("debuggerAddress",debugConfig.debugUrl)
        # 设置驱动位置
        service = Service(executable_path=debugConfig.webDriver)
        driver = webdriver.Chrome(service=service, options=options)
 
        # 在当前标签页进行新建标签页
        # driver.switch_to.new_window(WindowTypes.TAB)
    
        # driver.get("https://www.baidu.com")
        # time.sleep(5)
        # driver.quit()

        # 获取所有标签页的句柄
        handles = driver.window_handles
        # 切换到最后一个标签页
        driver.switch_to.window(handles[-1])
        driver.find_element(By.XPATH, "//button[@value='1']").click()
        time.sleep(5)
        driver.quit()
        pass


