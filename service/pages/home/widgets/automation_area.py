import flet as ft
from flet_core import ElevatedButton, Container, ResponsiveRow, Column, Ref

from service.utils.common_utils import CommonUtils


class AutomationArea(ft.UserControl):
    def __init__(self, parent: ft.Page):
        super().__init__()
        self.parent = parent

        self.btn_quick_account = Ref[ElevatedButton]()
        self.btn_quick_black_account = Ref[ElevatedButton]()
        self.btn_crawling_materials = Ref[ElevatedButton]()

    def build(self):

        return Container(
            width=self.parent.width,
            content=Column([
                Container(content=ft.Text("自动化", size=20), alignment=ft.alignment.center),
                ResponsiveRow([
                    ElevatedButton(
                        ref=self.btn_quick_account,
                        text="速拿二解号",
                        col={"sm": 4},
                        on_click=self.handle_onclick,
                    ),
                    ElevatedButton(
                        ref=self.btn_quick_black_account,
                        text="速拿大小黑",
                        col={"sm": 4},
                        on_click=self.handle_onclick,
                    ),
                    ElevatedButton(
                        ref=self.btn_crawling_materials,
                        text="爬取色色素材",
                        col={"sm": 4},
                        on_click=self.handle_onclick,
                    ),
                    ElevatedButton(
                        text="图片转视频",
                        col={"sm": 4},
                        on_click=self.handle_onclick,
                    ),
                    ElevatedButton(
                        text="视频极速换封面",
                        col={"sm": 4},
                        on_click=self.handle_onclick,
                    ),
                    ElevatedButton(
                        text="视频快速滤镜",
                        col={"sm": 4},
                        on_click=self.handle_onclick,
                    ),
                    ElevatedButton(
                        text="图片微调",
                        col={"sm": 4},
                        on_click=self.handle_onclick,
                    ),
                    ElevatedButton(
                        text="图片快速滤镜",
                        col={"sm": 4},
                        on_click=self.handle_onclick,
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ])
        )

    def handle_onclick(self, event: ft.ControlEvent):
        view = event.control
        viewText = view.text

        if viewText == self.btn_quick_account.current.text:
            self.parent.go("/quick_facebook_account")
            pass
        elif viewText == self.btn_quick_black_account.current.text:
            self.parent.go("/quick_black_account")
            pass
        elif viewText == self.btn_crawling_materials.current.text:
            CommonUtils.showAlertDialog(self.page, "还没写呢,你干嘛~~哎呦~~")
            pass
        else:
            print("click err")
            pass
