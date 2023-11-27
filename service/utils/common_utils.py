from typing import List

import flet as ft
from flet_core import MainAxisAlignment, Control


class CommonUtils():
    @staticmethod
    def showSnack(page: ft.Page, text: str):
        if page.snack_bar is None:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Hello, world!"),
                action="错误!",
            )
        page.snack_bar.content = ft.Text(text)
        page.snack_bar.open = True
        page.update()

    @staticmethod
    def showAlertDialog(page: ft.Page, content: str, title='提示', ):
        if page.dialog is None:
            page.dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text(title),
                content=ft.Text(content),
                actions=[
                    ft.TextButton("确定", on_click=lambda p: CommonUtils.closeAlertDialog(page, page.dialog)),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: print("dialog dismissed!"),
            )
        page.dialog.open = True
        page.update()

    @staticmethod
    def closeAlertDialog(page: ft.Page, dialog: ft.AlertDialog):
        dialog.open = False
        page.update()

    @staticmethod
    def showBottomSheet(page: ft.Page, widgetList: List[Control], title='提示', ):
        bs = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    controls=widgetList,
                    tight=True,
                    alignment=MainAxisAlignment.CENTER
                ),
                padding=10,
                width=page.width,
            ),
            open=True,
        )
        page.overlay.append(bs)
        bs.open = True
        page.update()

    @staticmethod
    def closeBottomSheet(page: ft.Page, bs: ft.BottomSheet):
        bs.open = False
        page.update()
