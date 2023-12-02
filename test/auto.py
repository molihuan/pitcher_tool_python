import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes

debugUrl = '127.0.0.1:56056',
webDriver = r'C:\\Users\\Administrator\\AppData\\Roaming\\adspower_global\\cwd_global\\chrome_119\\chromedriver.exe'

options = webdriver.ChromeOptions()
# 调试地址
options.add_experimental_option("debuggerAddress", '127.0.0.1:61398')
# 设置驱动位置
service = Service(executable_path=webDriver)
driver = webdriver.Chrome(options=options)

# 在当前标签页进行新建标签页
# driver.switch_to.new_window(WindowTypes.TAB)

# driver.get("https://www.baidu.com")
# time.sleep(5)
# driver.quit()

# 获取所有标签页的句柄
handles = driver.window_handles

print(handles)
print(handles[-1])
# 切换到最后一个标签页
driver.switch_to.window(handles[-1])

print(driver.current_url)
# driver.find_element(By.XPATH, "//button[@value='1']").click()
