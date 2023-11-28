from flet_core import UserControl, Page, Container, Column, ElevatedButton, ScrollMode, MainAxisAlignment, AppBar, Text, \
    colors, alignment, TextField, Row, ListTile, ControlEvent
from service.dao.data_manager import DataManager

from service.http.http import HttpUtils
from service.models.group_msg import GroupMsg
from service.utils.common_utils import CommonUtils
from service.utils.str_utils import StrUtils


class QuickFacebookAccountPage(UserControl):
    def __init__(self, parent: Page):
        super().__init__()
        self.parent = parent

    def initData(self):
        # self.selectedGroup = DataManager.getSelectedGroup(self.page)
        tt = DataManager.getGroupMsg(self.page)
        print(tt)

    def build(self):
        # self.initData()

        self.rawAccountMsgTF = TextField(
            hint_text="请粘贴在这里",
            multiline=True,
            min_lines=5,
            max_lines=10,
        )

        self.showGroupText: Text = Text("null")

        self.browserNameTF = TextField(
            hint_text="浏览器名称(可不填,默认为空)",
            width=self.parent.width / 2
        )

        return Container(
            content=Column([
                Text("请粘贴完整的二解信息", size=20),
                self.rawAccountMsgTF,
                Row([
                    ElevatedButton(text="选择分组", on_click=self.clcSelectGroup),
                    Text("当前分组为:"),
                    self.showGroupText,
                ]),
                self.browserNameTF,
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
        response = HttpUtils.queryPackets()  # 调用queryPackets方法
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
        saveResult = DataManager.setGroupMsg(self.page, groupMsg)
        self.selectedGroupMsg = groupMsg
        if not saveResult:
            print('保存失败,请联系开发者解决')
            return
        self.showGroupText.value = groupMsg.group_name
        self.update()
        print('保存成功')
        pass

    def handleCreateAccount(self, event):

        rawText = self.rawAccountMsgTF.value
        groupId = self.selectedGroupMsg.group_id
        browserName = self.browserNameTF.value

        if len(rawText.strip()) == 0:
            CommonUtils.showSnack(self.page, "二解信息为空")
            return
        if len(groupId.strip()) == 0:
            CommonUtils.showSnack(self.page, "请先选择分组")
            return
        facebookMsg = StrUtils.getFacebookAccountMsg(rawText)
        print(facebookMsg)
        creatResult = HttpUtils.creatFacebookUser(facebookMsg, groupId)
        accountId = creatResult['data']['id']
        print(accountId)
        HttpUtils.openBrowser(accountId)
        pass
