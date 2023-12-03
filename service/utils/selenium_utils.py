import time
from typing import Tuple
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumUtils():
    @staticmethod
    def waitView(driver:WebDriver,locator: Tuple[str, str],timeout=10,msg:str = None):
        wait = WebDriverWait(driver, timeout)
        view = wait.until(EC.presence_of_element_located(locator))
        if msg == None:
            print("找到:"+locator[0]+"--->"+locator[1])
        else:
            print("找到:"+msg)
            
        time.sleep(1)
        return view
