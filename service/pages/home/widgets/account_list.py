from flet import UserControl, Page, DataTable
from flet_core import border, Text, DataColumn, DataRow, DataCell, Row, ElevatedButton, Ref, Column, Container, \
    TextField, MainAxisAlignment, TextAlign

from service.dao.data_manager import DataManager
from service.http.http import HttpUtils
from service.models.group_msg import GroupMsg
from service.utils.common_utils import CommonUtils


class AccountList(UserControl):
    def __init__(self, parent: Page):
        super().__init__()
        self.parent = parent
        self.dataTableRef = Ref[DataTable]()
        self.accountPageIndex = 1
        self.accountPageIndexShowText = Ref[Text]()

    def did_mount(self):
        self.changeAccountPageIndex(self.accountPageIndex)
        pass

    def changeAccountPageIndex(self, pageIndex):
        dataJson = DataManager.getGroupMsg(self.page)
        if dataJson is None:
            return
        self.selectedGroupMsg = GroupMsg.from_json(dataJson)
        response = HttpUtils.getAccountList(self.selectedGroupMsg.group_id, pageIndex)
        if (response is None) or (response['code'] != 0):
            print("获取账号列表失败")
            return
        self.accountMsgList: list = response['data']['list']
        self.accountViewList = []
        for accountMsg in self.accountMsgList:
            dataRow = DataRow(
                cells=[
                    DataCell(Text(accountMsg['name'] + "|" + accountMsg['serial_number'])),
                    DataCell(
                        Row([
                            ElevatedButton(text="打开",
                                           on_click=lambda event, id=accountMsg['user_id']: self.handleOpenAccount(
                                               event, id)),
                            ElevatedButton(text="关闭",
                                           on_click=lambda event, id=accountMsg['user_id']: self.handleCloseAccount(
                                               event, id))
                        ])
                    ),
                ],
            )
            self.accountViewList.append(dataRow)

        self.dataTableRef.current.rows = self.accountViewList
        self.accountPageIndexShowText.current.value = self.accountPageIndex
        print("更新成功")
        self.update()
        pass

    def handleOpenAccount(self, event, user_id):
        print("打开", user_id)
        CommonUtils.showSnack(self.page, "正在使用吃奶的力气打开浏览器,请稍后几秒...")
        openResult = HttpUtils.openBrowser(user_id)
        if openResult['code'] != 0:
            CommonUtils.showSnack(self.page, "打开浏览器失败,请联系开发者")
            return
        print(openResult)

    def handleCloseAccount(self, event, user_id):
        print("关闭", user_id)
        CommonUtils.showSnack(self.page, "正在使劲关闭浏览器,请稍后...")
        result = HttpUtils.closeBrowser(user_id)
        if result['code'] != 0:
            CommonUtils.showSnack(self.page, "关闭浏览器失败,请联系开发者")
            return
        print(result)
        pass

    def handlePrePage(self, event):
        self.accountPageIndex -= 1
        if self.accountPageIndex < 1:
            self.accountPageIndex = 1
        self.changeAccountPageIndex(self.accountPageIndex)
        print(self.accountPageIndex)
        pass

    def handleSufPage(self, event):
        self.accountPageIndex += 1
        self.changeAccountPageIndex(self.accountPageIndex)
        print(self.accountPageIndex)
        pass

    def build(self):

        return Column(
            controls=[
                DataTable(
                    ref=self.dataTableRef,
                    width=self.parent.width,
                    border=border.all(2, "grey"),
                    border_radius=10,
                    vertical_lines=border.BorderSide(1, "grey"),
                    horizontal_lines=border.BorderSide(1, "grey"),
                    columns=[
                        DataColumn(Text("账号信息")),
                        DataColumn(Text("操作")),
                    ],
                ),
                Row(
                    controls=[
                        ElevatedButton(text="上一页", on_click=self.handlePrePage),
                        # TextField(width=70, text_align=TextAlign.CENTER),
                        Text(ref=self.accountPageIndexShowText, value=str(self.accountPageIndex)),
                        ElevatedButton(text="下一页", on_click=self.handleSufPage)
                    ],
                    alignment=MainAxisAlignment.CENTER
                )

            ]
        )
