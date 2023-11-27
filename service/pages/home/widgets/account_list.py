import flet as ft


class AccountList(ft.UserControl):
    def __init__(self, parent: ft.Page):
        super().__init__()
        self.parent = parent

    def build(self):
        return ft.DataTable(
            width=self.parent.width,
            border=ft.border.all(2, "grey"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, "grey"),
            horizontal_lines=ft.border.BorderSide(1, "grey"),
            columns=[
                ft.DataColumn(ft.Text("账号")),
                ft.DataColumn(ft.Text("操作")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("1111")),
                        ft.DataCell(
                            ft.Row([
                                ft.ElevatedButton(text="打开"),
                                ft.ElevatedButton(text="关闭")
                            ])
                        ),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("1111")),
                        ft.DataCell(
                            ft.Row([
                                ft.ElevatedButton(text="打开"),
                                ft.ElevatedButton(text="关闭")
                            ])
                        ),
                    ],
                ),

            ],
        )
