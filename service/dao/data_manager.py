from flet import Page
class DataManager():
    @staticmethod
    def setSelectedGroup(page:Page,value):
        return page.client_storage.set("SelectedGroup", value)
    @staticmethod
    def getSelectedGroup(page:Page):
        return page.client_storage.get("SelectedGroup")