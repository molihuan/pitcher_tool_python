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
    SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=4).click()
    SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=3).click()
    SeleniumUtils.waitView(driver,(By.CSS_SELECTOR,'button[value="Continue"]'),timeout=3).click()
    pass
except:

    pass









