from flet import View, Page
from flet_core import AppBar, Text, colors, ElevatedButton

from service.pages.home.view import HomePage
from service.pages.quick_facebook_account.view import QuickFacebookAccountPage


class AppRoutes():
    def __init__(self, page: Page):
        self.page = page

    def view_pop(self, view):
        # 移除最上层的视图
        self.page.views.pop()
        top_view = self.page.views[-1]
        # 显示最上层视图
        self.page.go(top_view.route)

    def route_change(self, route):
        self.page.views.clear()
        # 默认页面
        self.page.views.append(
            View(
                "/",
                [
                    HomePage(self.page),
                ],
            )
        )
        if self.page.route == "/about":
            self.page.views.append(
                View(
                    "/about",
                    [
                        AppBar(title=Text("关于"), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton("返回首页", on_click=lambda _: self.page.go("/")),
                    ],
                )
            )
        elif self.page.route == "/quick_facebook_account":
            self.page.views.append(
                View(
                    "/quick_facebook_account",
                    [
                        AppBar(title=Text("速拿二解号"), bgcolor=colors.SURFACE_VARIANT),
                        QuickFacebookAccountPage(self.page)
                    ],
                )
            )
            pass
        self.page.update()
