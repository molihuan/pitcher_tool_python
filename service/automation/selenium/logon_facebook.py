from selenium import webdriver

from service.models.browser_debug_config import BrowserDebugConfig
class LogonFacebook():
    @staticmethod
    def run(config:BrowserDebugConfig):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress",config.debugUrl)

        driver = webdriver.Chrome(options=options)
        pass
