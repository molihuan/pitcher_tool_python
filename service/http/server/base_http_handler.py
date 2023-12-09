from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from service.automation.playwright.login_consume_report import LogonConsumeReport
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
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ret = ResponseBody.success_json_encode('服务器正常!')
            self.wfile.write(ret)
        elif self.path.startswith('/quick_url?'):
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ret = ResponseBody.success_json_encode('服务器正常!')
            self.wfile.write(ret)
        elif self.path.startswith('/automation?'):

            url_parts = urlparse(self.path)
            query_params = parse_qs(url_parts.query)
            print(query_params)
            # 获取名为 "param1" 的参数值
            # param1 = query_params.get('param1', [''])[0]

            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ret = ResponseBody.success_json_encode('服务器正常!')
            self.wfile.write(ret)
        else:
            self.send_error(404, 'Not found')
        print('do_GET end')

    def end_headers(self):
        # self.send_header('Access-Control-Allow-Origin', '*')  # 允许任何来源的跨域请求
        # self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 允许跨域请求的方法
        # self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # 允许的请求头
        super().end_headers()
