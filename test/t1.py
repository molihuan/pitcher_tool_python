import flet as ft
from flet_core import MainAxisAlignment


def main(page: ft.Page):
    def bs_dismissed(e):
        print("Dismissed!")

    def show_bs(e):
        bs.open = True
        bs.update()

    def close_bs(e):
        bs.open = False
        bs.update()

    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.ListTile(
                        title=ft.Text("莫利欢"),
                        on_click=lambda _: print("666")
                    ),
                ],
                tight=True,
            ),
            padding=10,
            width=page.width,
        ),
        open=True,
        on_dismiss=bs_dismissed,
    )
    page.overlay.append(bs)
    page.add(ft.ElevatedButton("Display bottom sheet", on_click=show_bs))


ft.app(target=main)
