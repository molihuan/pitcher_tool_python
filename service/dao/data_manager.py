from flet import Page


class DataManager():
    @staticmethod
    def setGroupMsg(page: Page, value):
        return page.client_storage.set("GroupMsg", value)

    @staticmethod
    def getGroupMsg(page: Page):
        groupMsgDirt = page.client_storage.get("GroupMsg")
        return groupMsgDirt
