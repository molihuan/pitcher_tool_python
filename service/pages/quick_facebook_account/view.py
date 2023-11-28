
from flet_core import UserControl, Page, Container, Column, ElevatedButton, ScrollMode, MainAxisAlignment, AppBar, Text, \
    colors, alignment, TextField, Row,ListTile,ControlEvent
from service.dao.data_manager import DataManager

from service.http.http import HttpUtils
from service.utils.common_utils import CommonUtils
from service.utils.str_utils import StrUtils


class QuickFacebookAccountPage(UserControl):
    def __init__(self, parent: Page):
        super().__init__()
        self.parent = parent
    def initData(self):
        # self.selectedGroup = DataManager.getSelectedGroup(self.page)
        pass

    def build(self):
        self.initData()

        self.rawAccountMsgTF = TextField(
            hint_text="请粘贴在这里",
            multiline=True,
            min_lines=5,
            max_lines=10,
        )

        self.browserNameTF = TextField(
            hint_text="浏览器名称(可不填,默认为空)",
            width=self.parent.width / 2
        )

        self.showGroupText:Text = Text("当前分组为：")

        return Container(
            content=Column([
                Text("请粘贴完整的二解信息", size=20),
                self.rawAccountMsgTF,
                Row([
                    ElevatedButton(text="选择分组", on_click=self.selectGroup),
                    self.showGroupText,
                ]),
                Row([
                    self.browserNameTF
                ]),

                ElevatedButton(text="创建并打开",
                               on_click=self.handleCreateAccount),

            ],
                scroll=ScrollMode.ALWAYS,
                alignment=MainAxisAlignment.CENTER
            ),
            alignment=alignment.center

        )

    def selectGroup(self, event):
        response = HttpUtils.queryPackets()  # 调用queryPackets方法
        if response is None:
            print("获取分组信息失败")
            return

        groupList = response['data']['list']
        print(groupList)
        groupListView = []
        for groupItem in groupList:
            groupListView.append(
                ListTile(
                    title= Text(groupItem['group_name']),
                    data=groupItem['group_id'],
                    on_click=lambda event,gi = groupItem : self.saveGroupMsg(event,gi)
                )  
            )
            
        CommonUtils.showBottomSheet(self.page, groupListView)
    # 保存分组信息
    def saveGroupMsg(self,event:ControlEvent,groupMsg):
        saveResult = DataManager.setSelectedGroup(self.page,groupMsg)
        if not saveResult:
            print('保存失败')
            return
        # CommonUtils.closeBottomSheet(self.page,event.control)
        self.showGroupText.value = "当前分组为:"+groupMsg['group_name']
        self.update()
        print('保存成功')
        pass

    def handleCreateAccount(self, event):
        value = DataManager.getSelectedGroup(self.page)
        print(value)

        rawText = self.rawAccountMsgTF.value
        groupId = self.browserNameTF.value
        if len(rawText.strip()) == 0:
            CommonUtils.showSnack(self.page, "二解信息为空")
            return
        if len(groupId.strip()) == 0:
            CommonUtils.showSnack(self.page, "请先选择分组")
            return
        facebookMsg = StrUtils.getFacebookAccountMsg(rawText)
        print(facebookMsg)
        HttpUtils.creatFacebookUser(facebookMsg, groupId)
        pass
