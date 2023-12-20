from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import requests

from service.automation.playwright.browser.browser_automation import BrowserAutomation
from service.automation.playwright.browser.quick_msg import QuickMsg
from service.automation.playwright.browser.quick_url import QuickUrl

from service.automation.playwright.login_consume_report import LogonConsumeReport
from service.http.api import URL_BASE_AD_API
from service.http.server.response_body import ResponseBody


class BaseHttpHandler(SimpleHTTPRequestHandler):
    # 空代表所有地址都可以访问
    CLIENT_URL: str = ''
    CLIENT_PORT: int = 54111

    def do_OPTIONS(self):
        print("do_OPTIONS")
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
        self.end_headers()

    def do_GET(self):
        print(f'do_GET 请求路径为:{self.path}')
        # 处理 GET 请求
        if self.path == '/':
            self.path = '/info'
            self.do_GET()
            pass
        elif self.path.startswith('/adinterface/'):
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            fullURL = self.path.replace('/adinterface', URL_BASE_AD_API)
            response = requests.get(fullURL)
            data = response.json()

            if response.status_code == 200:
                ret = data
            else:
                ret = ResponseBody.error_json_encode('转发请求失败')

            self.wfile.write(ret)

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ret = ResponseBody.success_json_encode('服务器正常!')
            self.wfile.write(ret)

        # 信息展示
        elif self.path.startswith('/quick_msg?'):
            self.send_response(200)

            url_parts = urlparse(self.path)
            query_params = parse_qs(url_parts.query)
            browserId = query_params['browserId'][0]
            func = query_params['func'][0]
            print(browserId)
            print(func)
            # 根据方法名调用方法注意参数
            qu = QuickMsg()
            method = getattr(qu, func)
            method(browserId)

            self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ret = ResponseBody.success_json_encode('服务器正常!')
            self.wfile.write(ret)
        # 快速网址
        elif self.path.startswith('/quick_url?'):
            self.send_response(200)

            url_parts = urlparse(self.path)
            query_params = parse_qs(url_parts.query)
            browserId = query_params['browserId'][0]
            func = query_params['func'][0]
            print(browserId)
            print(func)
            # 根据方法名调用方法注意参数
            qu = QuickUrl()
            method = getattr(qu, func)
            method(browserId)

            self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ret = ResponseBody.success_json_encode('服务器正常!')
            self.wfile.write(ret)

        # 自动化
        elif self.path.startswith('/automation?'):
            self.send_response(200)

            url_parts = urlparse(self.path)
            query_params = parse_qs(url_parts.query)
            browserId = query_params['browserId'][0]
            func = query_params['func'][0]
            print(browserId)
            print(func)
            # 根据方法名调用方法注意参数
            ba = BrowserAutomation()
            method = getattr(ba, func)
            method(browserId)

            self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ret = ResponseBody.success_json_encode('服务器正常!')
            self.wfile.write(ret)

        else:
            self.send_error(404, 'Not found')
        print('do_GET end')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        print(post_data)

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        fullURL = self.path.replace('/adinterface', URL_BASE_AD_API)
        response = requests.post(fullURL, json=post_data)
        data = response.json()

        if response.status_code == 200:
            ret = data
        else:
            ret = ResponseBody.error_json_encode('转发请求失败')

        self.wfile.write(ret)

        pass

    def end_headers(self):
        # self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
        # self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
        # self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # 允许的请求头
        super().end_headers()
