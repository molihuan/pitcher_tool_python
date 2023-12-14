import time
from flet_core import UserControl, Page, Container, Column, ElevatedButton, ScrollMode, MainAxisAlignment, AppBar, Text, \
    colors, alignment, TextField, Row, ListTile, ControlEvent, Ref, Switch

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


class QuickBlackAccountPage(UserControl):
    def __init__(self, parent: Page):
        super().__init__()
        self.parent = parent

        self.rawAccountMsgTF = Ref[TextField]()
        self.showGroupText = Ref[Text]()
        self.browserNameTF = Ref[TextField]()
        self.autoFacebookSwitch = Ref[Switch]()

    def initData(self):
        dataJson = DataManager.getGroupMsg()
        if dataJson is None:
            return
        self.selectedGroupMsg = GroupMsg.from_json(dataJson)
        self.showGroupText.current.value = self.selectedGroupMsg.group_name
        self.update()

    def did_mount(self):
        # 挂载后调用
        self.initData()
        pass

    def build(self):
        return Container(
            content=Column([
                Text("请复制username ~ cookie", size=20),
                Text("没有username和password请先在表上填'空'，再复制", size=15, color='red'),
                TextField(
                    ref=self.rawAccountMsgTF,
                    hint_text="请粘贴在这里",
                    multiline=True,
                    min_lines=5,
                    max_lines=50,
                ),
                Row([
                    ElevatedButton(text="选择分组", on_click=self.clcSelectGroup),
                    Text("当前分组为:"),
                    Text(ref=self.showGroupText, value=""),
                ]),
                TextField(
                    ref=self.browserNameTF,
                    hint_text="浏览器名称(可不填,默认为空)",
                    width=self.parent.width / 2
                ),
                Row([
                    Switch(ref=self.autoFacebookSwitch, label="自动打开facebook", value=True),
                ]),
                ElevatedButton(text="创建并打开",
                               on_click=self.handleCreateAccount),
            ],
                scroll=ScrollMode.ALWAYS,
                alignment=MainAxisAlignment.CENTER
            ),
            alignment=alignment.center

        )

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
        saveResult = DataManager.setGroupMsg(groupMsg.to_json())
        self.selectedGroupMsg = groupMsg
        if not saveResult:
            print('保存失败,请联系开发者解决')
            return
        self.showGroupText.current.value = groupMsg.group_name
        self.update()
        print('保存成功')
        pass

    def handleCreateAccount(self, event):

        rawText = self.rawAccountMsgTF.current.value
        groupId = self.selectedGroupMsg.group_id
        browserName = self.browserNameTF.current.value

        if len(rawText.strip()) == 0:
            CommonUtils.showSnack(self.page, "大小黑信息为空")
            return
        if len(groupId.strip()) == 0:
            CommonUtils.showSnack(self.page, "请先选择分组")
            return

        facebookMsg: FacebookAccountMsg = StrUtils.getBlackFacebookAccountMsg(rawText)
        print(facebookMsg)
        createResult = HttpUtils.creatBlackFacebookUser(facebookMsg, groupId, browserName)

        if createResult['code'] != 0:
            CommonUtils.showSnack(self.page, "创建账号失败,请检查二解信息是否完整。或联系开发者")
            return
        CommonUtils.showSnack(self.page, "创建账号成功!正在使用吃奶的力气打开浏览器,请稍后几秒...")
        accountId = createResult['data']['id']
        print(accountId)
        openResult = HttpUtils.openBrowser(accountId)
        if openResult['code'] != 0:
            CommonUtils.showSnack(self.page, "打开浏览器失败,请联系开发者")
            return
        self.rawAccountMsgTF.current.value = ''
        self.update()

        print(openResult)

        bdc = BrowserDebugConfig(
            debugUrl=openResult['data']['ws']['selenium'],
            debugPort=openResult['data']['debug_port'],
            webDriver=openResult['data']['webdriver'],
            debugWsUrl=openResult['data']['ws']['puppeteer'],
            browserId=accountId,
        )
        # 打开中控面板
        # CenterControlPanel.run(None, bdc)

        if self.autoFacebookSwitch.current.value:
            # 自动登录facebook
            # LogonFacebook.run(facebookMsg, bdc)
            # QuickUrl.openFacebookMainPage(browserId=bdc.browserId)
            pass
