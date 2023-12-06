from http.server import HTTPServer

from flet import Page, CrossAxisAlignment, app_async, app

from service.dao.data_manager import DataManager
from service.http.http import HttpUtils
from service.http.server.base_http_handler import BaseHttpHandler
from service.routes.app_routes import AppRoutes


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
    # 启动服务器
    server_address = ('', 5411)
    httpd = HTTPServer(server_address, BaseHttpHandler)
    print("Serving HTTP on port 5411...")
    httpd.serve_forever()


app(target=main)
