import socketserver
from http.server import HTTPServer

from flet import Page, CrossAxisAlignment, app_async, app

from service.dao.data_manager import DataManager
from service.http.http import HttpUtils
from service.http.server.base_http_handler import BaseHttpHandler
from service.routes.app_routes import AppRoutes
from service.utils.file_utils import FileUtils


def main(page: Page):
    page.title = "几何专用"
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    HttpUtils.setDebug(True)

    DataManager.setPage(page)

    # 路由配置
    appRoutes = AppRoutes(page)
    page.on_route_change = appRoutes.route_change
    page.on_view_pop = appRoutes.view_pop
    page.go(page.route)

    # 启动服务器地址和端口
    server_address = (BaseHttpHandler.CLIENT_URL, BaseHttpHandler.CLIENT_PORT)
    
    with socketserver.TCPServer(server_address, BaseHttpHandler) as httpd:
        print(f"服务器已启动，通过 http://127.0.0.1:{BaseHttpHandler.CLIENT_PORT} 访问")
        httpd.serve_forever()


app(target=main)
