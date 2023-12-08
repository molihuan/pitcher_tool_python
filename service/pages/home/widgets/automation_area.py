import flet as ft
from flet_core import ElevatedButton, Container, ResponsiveRow, Column, Ref


class AutomationArea(ft.UserControl):
    def __init__(self, parent: ft.Page):
        super().__init__()
        self.parent = parent

        self.btn_quick_account = Ref[ElevatedButton]()
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
                        ref=self.btn_crawling_materials,
                        text="爬取素材",
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
        elif viewText == self.btn_crawling_materials.current.text:
            pass
        else:
            print("click err")
            pass
