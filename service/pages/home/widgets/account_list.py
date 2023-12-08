from flet import UserControl, Page, DataTable
from flet_core import border, Text, DataColumn, DataRow, DataCell, Row, ElevatedButton, Ref, Column, Container, \
    TextField, MainAxisAlignment, TextAlign, ListTile, ControlEvent, OutlinedButton
from service.automation.playwright.center_control_panel import CenterControlPanel

from service.dao.data_manager import DataManager
from service.http.http import HttpUtils
from service.models.browser_debug_config import BrowserDebugConfig
from service.models.group_msg import GroupMsg
from service.utils.common_utils import CommonUtils


class AccountList(UserControl):
    def __init__(self, parent: Page):
        super().__init__()
        self.selectedGroupMsg = GroupMsg()
        self.parent = parent
        self.dataTableRef = Ref[DataTable]()
        self.accountPageIndex = 1
        self.accountPageIndexShowText = Ref[Text]()
        self.showGroupBtn = Ref[OutlinedButton]()

    def initData(self):
        dataJson = DataManager.getGroupMsg(self.page)
        if dataJson is None:
            return
        self.selectedGroupMsg = GroupMsg.from_json(dataJson)
        self.showGroupBtn.current.text = "分组:" + self.selectedGroupMsg.group_name
        self.update()

    # 点击选择分组按钮
    def clcSelectGroup(self, event):
        # 查询分组信息
        response = HttpUtils.queryPackets()
        if response is None:
            print("获取分组信息失败")
            return

        groupMsgList = response['data']['list']
        print(groupMsgList)
        groupListView = []
        for groupItem in groupMsgList:
            groupMsg = GroupMsg(groupItem['group_id'], groupItem['group_name'])
            groupListView.append(
                ListTile(
                    title=Text(groupMsg.group_name),
                    data=groupMsg.group_id,
                    on_click=lambda event, gi=groupMsg: self.clcGroupItem(event, gi)
                )
            )
        # 显示底部弹窗
        self.bs = CommonUtils.showBottomSheet(self.page, groupListView)

    # 点击分组Item信息
    def clcGroupItem(self, event: ControlEvent, groupMsg: GroupMsg):
        CommonUtils.closeBottomSheet(self.page, self.bs)
        # 持久化
        saveResult = DataManager.setGroupMsg(self.page, groupMsg.to_json())
        self.selectedGroupMsg = groupMsg
        if not saveResult:
            print('保存失败,请联系开发者解决')
            return
        self.showGroupBtn.current.text = "分组:" + self.selectedGroupMsg.group_name
        self.changeAccountPageIndex(1)
        self.update()
        print('保存成功')
        pass

    def did_mount(self):
        self.initData()
        self.changeAccountPageIndex(self.accountPageIndex)
        pass

    # 改变页面索引
    def changeAccountPageIndex(self, pageIndex):

        response = HttpUtils.getAccounts(group_id=self.selectedGroupMsg.group_id, page=pageIndex)
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
                                               event, id)),
                            ElevatedButton(text="面板",
                                           on_click=lambda event, id=accountMsg['user_id']: self.handleOpenPanel(
                                               event, id)),
                        ])
                    ),
                ],
            )
            self.accountViewList.append(dataRow)
        if len(self.accountViewList) == 0:
            CommonUtils.showSnack(self.page, "最后一页了!我也是有底线的")
            self.accountPageIndex -= 1
            return
        self.dataTableRef.current.rows = self.accountViewList
        self.accountPageIndexShowText.current.value = self.accountPageIndex
        print("更新成功")
        self.update()
        pass

    # 打开账号
    def handleOpenAccount(self, event, user_id):
        print("打开", user_id)
        CommonUtils.showSnack(self.page, "正在使用吃奶的力气打开浏览器,请稍后几秒...")
        openResult = HttpUtils.openBrowser(user_id)
        if openResult['code'] != 0:
            CommonUtils.showSnack(self.page, "打开浏览器失败,请联系开发者")
            return
        bdc = BrowserDebugConfig(
            debugUrl=openResult['data']['ws']['selenium'],
            debugPort=openResult['data']['debug_port'],
            webDriver=openResult['data']['webdriver'],
            debugWsUrl=openResult['data']['ws']['puppeteer'],
        )
        print(bdc)
        # LogonFacebook.run(bdc)

    # 关闭账号
    def handleCloseAccount(self, event, user_id):
        print("关闭", user_id)
        CommonUtils.showSnack(self.page, "正在使劲关闭浏览器,请稍后...")
        result = HttpUtils.closeBrowser(user_id)
        if result['code'] != 0:
            CommonUtils.showSnack(self.page, "关闭浏览器失败,请联系开发者")
            return
        print(result)
        pass

    # 打开中控面板
    def handleOpenPanel(self, event, user_id):
        status = HttpUtils.startupStatus(user_id)
        statusData = status['data']
        if (status['code'] != 0):
            print('获取状态失败')
            return
        if (statusData['status'] != 'Active'):
            print('浏览器未打开')
            return
        debugWsUrl = statusData['ws']['puppeteer']
        CenterControlPanel.run(None, BrowserDebugConfig(debugWsUrl=debugWsUrl))
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
                        DataColumn(
                            Row(
                                controls=[
                                    Text("账号信息"),
                                    OutlinedButton(ref=self.showGroupBtn, text="分组:", on_click=self.clcSelectGroup),
                                ]
                            )
                        ),
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
