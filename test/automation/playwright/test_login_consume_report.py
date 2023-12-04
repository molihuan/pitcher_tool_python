import sys
import time
from urllib import response
import pyotp
from playwright.sync_api import sync_playwright


sys.path.append('E:\\software\\python\\Project\\pitcher_tool_python')
from service.automation.playwright.login_consume_report import LogonConsumeReport

LogonConsumeReport.run()