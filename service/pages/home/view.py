import flet as ft

from service.automation.playwright.login_consume_report import LogonConsumeReport
from service.pages.home.widgets.account_list import AccountList
from service.pages.home.widgets.automation_area import AutomationArea
from service.pages.home.widgets.quick_dir_file import QuickDirFile
from service.pages.home.widgets.quick_website import QuickWebsite
from service.utils.common_utils import CommonUtils


class HomePage(ft.UserControl):
    def __init__(self, parent: ft.Page):
        super().__init__()
        self.parent = parent

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    AccountList(self.parent),
                    ft.ElevatedButton(text="测试按钮1",
                                      on_click=lambda _: self.todo()),
                    AutomationArea(self.parent),
                    QuickWebsite(self.parent),
                    QuickDirFile(self.parent),
                ],
                auto_scroll=True,
                scroll=ft.ScrollMode.ALWAYS,
                alignment=ft.MainAxisAlignment.CENTER
            ),
        )

    def todo(self):
        CommonUtils.showAlertDialog(self.page, "还没写呢,你干嘛~~哎呦~~")
