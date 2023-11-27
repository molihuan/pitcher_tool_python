import flet as ft

from service.pages.home.view import HomePage
from service.routes.app_routes import AppRoutes


def main(page: ft.Page):
    page.title = "超级投手工具"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 路由配置
    appRoutes = AppRoutes(page)
    page.on_route_change = appRoutes.route_change
    page.on_view_pop = appRoutes.view_pop
    page.go(page.route)


ft.app(target=main)
