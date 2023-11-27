import os

import chardet
import flet as ft
import pandas as pd
from flet_core import ElevatedButton, ResponsiveRow, Text, Row, ListView, IconButton
from pandas import DataFrame

from service.utils.common_utils import CommonUtils
from service.utils.file_utils import FileUtils


class QuickDirFile(ft.UserControl):
    def __init__(self, parent: ft.Page):
        super().__init__()
        self.parent = parent
        # 获取配置文件地址
        self.configExcelPath = os.path.join(FileUtils.getAssetsPath(), "ShortcutDirFileConfig.xlsx")

    def build(self):
        self.initData()
        return ListView([
            Row([
                Text("快捷文件/文件夹", size=20),
                IconButton(
                    icon=ft.icons.SETTINGS,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="快捷文件/文件夹自定义",
                    on_click=lambda p: FileUtils.open_file_or_folder(self.configExcelPath)
                )
            ]),
            ResponsiveRow(self.shortcutDirFileBtnList, alignment=ft.MainAxisAlignment.START),
        ])

    def initData(self):
        # 读取Excel文件
        df: DataFrame = pd.read_excel(self.configExcelPath)
        self.shortcutDirFileBtnList = []

        for index, row in df.iterrows():
            print(row.iloc[0], row.iloc[1])
            btnItem = ElevatedButton(
                text=row.iloc[0],
                col={"sm": 4},
                # 必须复制一份dirFilePath=row[1]
                on_click=lambda event, dirFilePath=row.iloc[1]: self.openDirFile(event, dirFilePath),
            )
            self.shortcutDirFileBtnList.append(btnItem)

    def openDirFile(self, event, dirFilePath):
        print(event)
        if not FileUtils.exists(dirFilePath):
            CommonUtils.showSnack(self.page, "路径不存在,请检查Excel配置")
        FileUtils.open_file_or_folder(dirFilePath)
        pass
