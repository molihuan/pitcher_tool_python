import time
from flet_core import UserControl, Page, Container, Column, ElevatedButton, ScrollMode, MainAxisAlignment, AppBar, Text, \
    colors, alignment, TextField, Row, ListTile, ControlEvent, Ref, Switch,FilePicker

from service.automation.playwright.browser.quick_url import QuickUrl
from service.automation.playwright.center_control_panel import CenterControlPanel
from service.automation.playwright.login_outlook import LoginOutlook
from service.automation.playwright.logon_facebook import LogonFacebook
from service.dao.data_manager import DataManager

from service.http.http import HttpUtils
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.facebook_account_msg import FacebookAccountMsg
from service.models.group_msg import GroupMsg
from service.utils.common_utils import CommonUtils
from service.utils.str_utils import StrUtils


class QuickVideoCoverPage(UserControl):
    def __init__(self, parent: Page):
        super().__init__()
        self.parent = parent

    def initData(self):
        pass

    def did_mount(self):
        # 挂载后调用
        self.initData()
        pass
    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)

        file_picker = FilePicker(on_result=on_dialog_result)
    
    def selectVideoPath(self):
        pass

    def build(self):
        return Container(
            content=Column([
                Row([
                    TextField(),
                    ElevatedButton('选择视频')
                ]),
                Row([
                    TextField(),
                    ElevatedButton('选择封面')
                ]),
            ],
                scroll=ScrollMode.ALWAYS,
                alignment=MainAxisAlignment.CENTER
            ),
            alignment=alignment.center

        )

    