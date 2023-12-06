from flet import Page


class DataManager():
    page: Page = None

    @staticmethod
    def setPage(page: Page):
        DataManager.page = page

    @staticmethod
    def setGroupMsg(page: Page, value):
        return page.client_storage.set("MLH_GroupMsg", value)

    @staticmethod
    def getGroupMsg(page: Page):
        groupMsgDirt = page.client_storage.get("MLH_GroupMsg")
        return groupMsgDirt

    @staticmethod
    def setBrowserPath(value):
        return DataManager.page.client_storage.set("MLH_BrowserPath", value)

    @staticmethod
    def getBrowserPath():
        groupMsgDirt = DataManager.page.client_storage.get("MLH_BrowserPath")
        return groupMsgDirt
