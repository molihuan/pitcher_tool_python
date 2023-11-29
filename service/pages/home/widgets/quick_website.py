import os

import flet as ft

from flet_core import ElevatedButton, Container, ResponsiveRow, Column, ListView, Row, Text, IconButton
from openpyxl import load_workbook

from service.utils.file_utils import FileUtils
from service.utils.web_utils import WebUtils


class QuickWebsite(ft.UserControl):
    def __init__(self, parent: ft.Page):
        super().__init__()
        self.parent = parent
        # 获取配置文件地址
        self.configExcelPath = os.path.join(FileUtils.getAssetsPath(), "ShortcutWebsiteConfig.xlsx")

    def build(self):
        self.initData()
        return ListView([
            Row([
                Text("快捷网址", size=20),
                IconButton(
                    icon=ft.icons.SETTINGS,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="快捷网址自定义",
                    on_click=lambda p: FileUtils.open_file_or_folder(self.configExcelPath)
                )
            ]),
            ResponsiveRow(self.shortcutWebsiteBtnList, alignment=ft.MainAxisAlignment.START),
        ])

    def initData(self):
        self.shortcutWebsiteBtnList = []
        wb = load_workbook(filename=self.configExcelPath)

        ws = wb.active
        for cells in ws.iter_rows(min_row=2):  # 从第二行开始遍历
            print(cells[0].value, cells[1].value)
            btnItem = ElevatedButton(
                text=cells[0].value,
                col={"sm": 4},
                # 必须复制一份dirFilePath=row[1]
                on_click=lambda event, url=cells[1].value: self.openWebsite(event, url),
            )
            self.shortcutWebsiteBtnList.append(btnItem)

        # 读取Excel文件
        # df: DataFrame = pd.read_excel(self.configExcelPath)
        # self.shortcutWebsiteBtnList = []
        #
        # for index, row in df.iterrows():
        #     print(row.iloc[0], row.iloc[1])
        #     btnItem = ElevatedButton(
        #         text=row.iloc[0],
        #         col={"sm": 4},
        #         # 必须复制一份dirFilePath=row[1]
        #         on_click=lambda event, url=row.iloc[1]: self.openWebsite(event, url),
        #     )
        #     self.shortcutWebsiteBtnList.append(btnItem)

    def openWebsite(self, event, url):
        print(event)
        WebUtils.open_url(url)
        pass
