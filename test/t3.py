from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")
driver.close()
