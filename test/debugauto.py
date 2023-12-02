import time

from selenium import webdriver

# 创建一个Chrome WebDriver实例
from selenium.webdriver.common.window import WindowTypes

driver = webdriver.Chrome()

# 获取调试地址
debug_url = driver.command_executor._url

print("调试地址:", debug_url)

driver.get("https://www.bilibili.com/")

driver.switch_to.new_window(WindowTypes.TAB)

driver.get("https://www.baidu.com")

# 获取所有标签页的句柄
handles = driver.window_handles

print(handles)

# 切换到最后一个标签页
driver.switch_to.window(handles[1])

print(driver.current_url)

driver.close()
