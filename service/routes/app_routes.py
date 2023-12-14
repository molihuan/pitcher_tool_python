from flet import View, Page
import flet as ft
from flet_core import AppBar, Text, colors, ElevatedButton, ScrollMode

from service.pages.home.view import HomePage
from service.pages.home.widgets.home_popup_menuitems import HomePopupMenuItems
from service.pages.quick_black_account.view import QuickBlackAccountPage
from service.pages.quick_facebook_account.view import QuickFacebookAccountPage
from service.pages.quick_video_cover.view import QuickVideoCoverPage
from service.utils.common_utils import CommonUtils


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
                scroll=ScrollMode.AUTO,
                appbar=ft.AppBar(
                    # leading=ft.Image(src=f"/imgs/ml.png"),
                    # leading_width=40,
                    title=ft.Text("投手工具"),
                    center_title=False,
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    actions=[
                        ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,
                                      on_click=lambda _: CommonUtils.showAlertDialog(self.page, "你干嘛~~哎呦~~")),
                        HomePopupMenuItems(),
                    ],
                )
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
        elif self.page.route == "/quick_black_account":
            self.page.views.append(
                View(
                    "/quick_black_account",
                    [
                        AppBar(title=Text("速拿大小黑"), bgcolor=colors.SURFACE_VARIANT),
                        QuickBlackAccountPage(self.page)
                    ],
                )
            )
            pass
        elif self.page.route == "/quick_video_cover":
            self.page.views.append(
                View(
                    "/quick_video_cover",
                    [
                        AppBar(title=Text("视频极速换封面"), bgcolor=colors.SURFACE_VARIANT),
                        QuickVideoCoverPage(self.page)
                    ],
                )
            )
            pass
        self.page.update()
