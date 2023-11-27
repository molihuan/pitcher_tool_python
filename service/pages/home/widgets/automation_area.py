import flet as ft
from flet_core import ElevatedButton, Container, ResponsiveRow, Column


class AutomationArea(ft.UserControl):
    def __init__(self, parent: ft.Page):
        super().__init__()
        self.parent = parent

    def build(self):
        self.btn_quick_account = ElevatedButton(
            text="速拿二解号",
            col={"sm": 4},
            on_click=self.handle_onclick,
        )
        self.btn_verifica_code = ElevatedButton(
            text="自动输入二次验证码",
            col={"sm": 4},
            on_click=self.handle_onclick,
        )
        self.btn_logon_email = ElevatedButton(
            text="自动登录邮箱",
            col={"sm": 4},
            on_click=self.handle_onclick,
        )
        self.btn_authorize_note_homepage = ElevatedButton(
            text="自动授权主页并登记授权主页",
            col={"sm": 4},
            on_click=self.handle_onclick,
        )

        self.btn_replace_homepage_img = ElevatedButton(
            text="自动替换主页‘茶’背景和头像",
            col={"sm": 4},
            on_click=self.handle_onclick,
        )

        self.btn_fill_account_info = ElevatedButton(
            text="自动填写开户信息",
            col={"sm": 4},
            on_click=self.handle_onclick,
        )
        self.btn_wechat_send_msg = ElevatedButton(
            text="微信自动发消息@某人",
            col={"sm": 4},
            on_click=self.handle_onclick,
        )

        return Container(
            width=self.parent.width,
            content=Column([
                Container(content=ft.Text("自动化", size=20), alignment=ft.alignment.center),
                ResponsiveRow([
                    self.btn_quick_account,
                    self.btn_verifica_code,
                    self.btn_logon_email,
                    self.btn_authorize_note_homepage,
                    self.btn_replace_homepage_img,
                    self.btn_fill_account_info,
                    self.btn_wechat_send_msg,
                ], alignment=ft.MainAxisAlignment.CENTER)
            ])
        )

    def handle_onclick(self, event: ft.ControlEvent):
        view = event.control
        print(view.text)

        if view == self.btn_quick_account:
            self.parent.go("/quick_facebook_account")
            pass
        elif view == self.btn_verifica_code:
            pass
        elif view == self.btn_logon_email:
            pass
        elif view == self.btn_authorize_note_homepage:
            pass
        elif view == self.btn_replace_homepage_img:
            pass
        elif view == self.btn_fill_account_info:
            pass
        elif view == self.btn_wechat_send_msg:
            pass
        else:
            print("click err")
            pass
