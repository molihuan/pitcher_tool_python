from flet_core import UserControl, Page, Container, Column, ElevatedButton, ScrollMode, MainAxisAlignment, AppBar, Text, \
    colors, alignment, TextField, Row

from service.utils.common_utils import CommonUtils
from service.utils.str_utils import StrUtils


class QuickFacebookAccountPage(UserControl):
    def __init__(self, parent: Page):
        super().__init__()
        self.parent = parent

    def build(self):
        self.rawAccountMsgTextField = TextField(
            hint_text="请粘贴在这里",
            multiline=True,
            min_lines=5,
            max_lines=10,
        )

        return Container(
            content=Column([
                Text("请粘贴完整的二解信息", size=20),
                self.rawAccountMsgTextField,
                Row([
                    ElevatedButton(text="选择分组", on_click=lambda _: CommonUtils.showBottomSheet(self.page, "你干嘛~~哎呦~~")),
                    Text("当前分组为"),
                ]),
                Row([
                    TextField(
                        hint_text="浏览器名称(可不填,默认为空)",
                        width=self.parent.width / 2
                    ),
                ]),

                ElevatedButton(text="创建并打开",
                               on_click=self.handleCreateAccount),

            ],
                scroll=ScrollMode.ALWAYS,
                alignment=MainAxisAlignment.CENTER
            ),
            alignment=alignment.center

        )

    def handleCreateAccount(self, event):
        rawText = self.rawAccountMsgTextField.value
        if len(rawText.strip()) == 0:
            CommonUtils.showSnack(self.page, "二解信息为空")
            return
        facebookMsg = StrUtils.getFacebookAccountMsg(rawText)
        print(facebookMsg)
        pass
