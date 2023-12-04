from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

from service.http.server.response_body import ResponseBody


class BaseHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 处理 GET 请求
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ret = ResponseBody.success_json_encode('服务器正常运行!')
            self.wfile.write(ret)
        else:
            self.send_error(404, 'File not found.')

    def do_POST(self):
        # 获取请求的长度
        content_length = int(self.headers['Content-Length'])
        # 读取请求的内容
        post_data = self.rfile.read(content_length)
        # 解析请求内容
        data = parse_qs(post_data.decode('utf-8'))

        # 发送响应
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(data).encode('utf-8'))
