from flet_core import UserControl, PopupMenuButton, PopupMenuItem, AlertDialog, MainAxisAlignment, TextButton, \
    TextField, Text, Ref

from service.dao.data_manager import DataManager
from service.utils.common_utils import CommonUtils


class HomePopupMenuItems(UserControl):
    def __init__(self):
        super().__init__()
        self.selectBrowserTF = Ref[TextField]()

    def build(self):
        return PopupMenuButton(
            items=[
                PopupMenuItem(text="设置浏览器路径", on_click=lambda _: self.clcSelectBrowserDialog()),
                PopupMenuItem(),  # divider
                PopupMenuItem(text="重置设置", on_click=lambda _: self.page.client_storage.clear()),
            ]
        )

    def clcSelectBrowserDialog(self):
        CommonUtils.showAlertDialog(page=self.page,
                                    titleStr='设置浏览器路径',
                                    content=TextField(
                                        ref=self.selectBrowserTF,
                                    ),
                                    actions=[
                                        TextButton("确定", on_click=self.selectBrowserOk),
                                        TextButton("取消", on_click=lambda p: CommonUtils.closeAlertDialog(self.page,
                                                                                                         self.page.dialog)),
                                    ], )

        browserPath = DataManager.getBrowserPath(self.page)
        print(browserPath)
        self.selectBrowserTF.current.value = browserPath
        self.update()

    def selectBrowserOk(self, event):
        browserPath = self.selectBrowserTF.current.value
        print(browserPath)
        DataManager.setBrowserPath(self.page, browserPath)
        pass

    def did_mount(self):
        pass
