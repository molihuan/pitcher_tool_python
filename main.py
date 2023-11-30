import flet as ft

from service.http.http import HttpUtils
from service.pages.home.view import HomePage
from service.routes.app_routes import AppRoutes


def main(page: ft.Page):
    page.title = "几何专用"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    HttpUtils.setDebug(False)

    # 路由配置
    appRoutes = AppRoutes(page)
    page.on_route_change = appRoutes.route_change
    page.on_view_pop = appRoutes.view_pop
    page.go(page.route)


ft.app(target=main)
