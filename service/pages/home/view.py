import flet as ft

from service.pages.home.widgets.account_list import AccountList
from service.pages.home.widgets.automation_area import AutomationArea
from service.pages.home.widgets.quick_dir_file import QuickDirFile
from service.pages.home.widgets.quick_website import QuickWebsite
from service.utils.common_utils import CommonUtils

# from flet_contrib.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}


class HomePage(ft.UserControl):
    def __init__(self, parent: ft.Page):
        super().__init__()
        self.parent = parent

    def build(self):
        # button = ft.ElevatedButton("Toast", 
        #     on_click=lambda _: ToastsFlexible(
        #         page=page,
        #         icon=ft.icons.INFO,
        #         title="Toast without trigger",
        #         desc="Toast description",
        #         auto_close=None,
        #         trigger=None,
        #         set_history=toasts_history,
        #         position=ToastPosition.TOP_RIGHT,
        #         actions=[
        #             ToastAction(
        #                 text="action",
        #                 action_style="texted",
        #                 on_click=lambda e: print(toasts_history),
        #             )
        #         ]
        #     )
        # )





        return ft.Container(
            content=ft.Column(
                [
                    AccountList(self.parent),
                    ft.ElevatedButton(text="测试按钮1",
                                      on_click=lambda _: CommonUtils.showAlertDialog(self.page, "你干嘛~~哎呦~~")),
                    # ft.ElevatedButton(text="重置设置",
                    #                   on_click=lambda _: self.page.client_storage.clear()),
                    # button,
                    AutomationArea(self.parent),
                    QuickWebsite(self.parent),
                    QuickDirFile(self.parent),
                ],
                auto_scroll=True,
                scroll=ft.ScrollMode.ALWAYS,
                alignment=ft.MainAxisAlignment.CENTER
            ),
        )
