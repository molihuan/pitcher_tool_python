import sys
import time
from urllib import response
import pyotp



sys.path.append('E:\\software\\python\\Project\\pitcher_tool_python')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from service.utils.str_utils import StrUtils
from service.models.browser_debug_config import BrowserDebugConfig
from service.http.http import HttpUtils
from service.utils.selenium_utils import SeleniumUtils
from service.models.facebook_account_msg import FacebookAccountMsg



webDriverPath = r'C:\\Users\\Administrator\\AppData\\Roaming\\adspower_global\\cwd_global\\chrome_119\\chromedriver.exe'

user_id='jc6r8us'

# 获取账户是否打开状态
status=HttpUtils.startupStatus(user_id)

print(status)

if (status == None) or (status['code']!=0) or (status['data']['status']!="Active"):
    print("获取状态失败")

# 获取调试地址
debugUrl=status['data']['ws']['selenium']
debugConfig = BrowserDebugConfig(debugUrl=debugUrl,webDriver=webDriverPath)

# 获取用户信息
accountResp=HttpUtils.getAccounts(user_id=user_id,page=1)
if (status == None) or (status['code']!=0) :
    print("用户信息获取失败")
firstAccount = accountResp['data']['list'][0]
print(firstAccount)

facebookMsg=StrUtils.getFacebookAccountMsgByRemark(firstAccount['remark'])
facebookMsg.userName=firstAccount['username']
facebookMsg.userPwd=firstAccount['password']


##################################################
options = webdriver.ChromeOptions()
# 调试地址
options.add_experimental_option("debuggerAddress", debugConfig.debugUrl)
# 设置驱动位置
service = Service(executable_path=debugConfig.webDriver)
driver = webdriver.Chrome(options=options)
###################################################
# 在当前标签页进行新建标签页
# driver.switch_to.new_window(WindowTypes.TAB)

# driver.get("https://www.baidu.com")
# time.sleep(5)
# driver.quit()

# 新建一个facebook标签
# driver.switch_to.new_window(WindowTypes.TAB)
# driver.get("https://facebook.com")

# 获取所有标签页的句柄
# handles = driver.window_handles
# 切换到最后一个标签页
# driver.switch_to.window(handles[-1])


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
    # 辅助邮箱
    SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="iShowSkip"]'),timeout=3).click()
except:

    pass
time.sleep(1)
try:
    # 保持登录状态?
    SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="acceptButton"]'),timeout=2).click()
except:
    # 保持登录状态?
    SeleniumUtils.waitView(driver,(By.XPATH,'//*[@id="idSIButton9"]'),timeout=3).click()
    pass

time.sleep(1)

try:
    # 摆脱密码束缚
    driver.find_element(By.XPATH,'//*[@id="iCancel"]').click()
except:
    pass






