from flet import Page


class DataManager():
    @staticmethod
    def setGroupMsg(page: Page, value):
        return page.client_storage.set("MLH_GroupMsg", value)

    @staticmethod
    def getGroupMsg(page: Page):
        groupMsgDirt = page.client_storage.get("MLH_GroupMsg")
        return groupMsgDirt

    @staticmethod
    def setBrowserPath(page: Page, value):
        return page.client_storage.set("MLH_BrowserPath", value)

    @staticmethod
    def getBrowserPath(page: Page):
        groupMsgDirt = page.client_storage.get("MLH_BrowserPath")
        return groupMsgDirt
