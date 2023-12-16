import time
from os import path

from flet_core import UserControl, Page, Container, Column, ElevatedButton, ScrollMode, MainAxisAlignment, AppBar, Text, \
    colors, alignment, TextField, Row, ListTile, ControlEvent, Ref, Switch, FilePicker, FilePickerResultEvent
from service.utils.common_utils import CommonUtils

from service.utils.ffmpeg_utils import FFmpegUtils
from service.utils.file_utils import FileUtils
from service.utils.str_utils import StrUtils


class QuickVideoCoverPage(UserControl):
    def __init__(self, parent: Page):
        super().__init__()
        self.parent = parent
        self.btn_select_video_path = Ref[ElevatedButton]()
        self.btn_select_img_path = Ref[ElevatedButton]()
        self.tf_select_video_path = Ref[TextField]()
        self.tf_select_img_path = Ref[TextField]()

        self.btn_run_ffmpeg = Ref[ElevatedButton]()

        self.btn_select_path_type = self.btn_select_video_path

    def initData(self):
        self.file_picker = FilePicker(on_result=self.on_select_result)
        self.page.overlay.append(self.file_picker)
        self.page.update()
        pass

    def did_mount(self):
        # 挂载后调用
        self.initData()
        pass

    def on_select_result(self, e: FilePickerResultEvent):

        if self.btn_select_path_type == self.btn_select_video_path:
            if e.files == None:
                print('选择视频取消了')
                return
            print("视频文件:", e.files)
            self.tf_select_video_path.current.value = e.files[0].path
            self.tf_select_video_path.current.update()
            pass
        elif self.btn_select_path_type == self.btn_select_img_path:
            if e.files == None:
                print('选择视频取消了')
                return
            print("封面文件:", e.files)
            self.tf_select_img_path.current.value = e.files[0].path
            self.tf_select_img_path.current.update()
            pass
        else:
            print("click err")
            pass

    def btn_click(self, e: ControlEvent):
        view = e.control
        viewText = view.text

        if viewText == self.btn_select_video_path.current.text:
            self.btn_select_path_type = self.btn_select_video_path
            # 打开选择器,单选
            self.file_picker.pick_files(dialog_title='选择视频', allow_multiple=False)
            pass
        elif viewText == self.btn_select_img_path.current.text:
            self.btn_select_path_type = self.btn_select_img_path
            self.file_picker.pick_files(dialog_title='选择封面', allow_multiple=False)
            pass
        elif viewText == self.btn_run_ffmpeg.current.text:
            ffmpegExec = path.join(FileUtils.getAssetsPath(), 'ffmpeg\\ffmpeg.exe')
            #检查是否存在空格
            videoPath = self.tf_select_video_path.current.value
            imgPath = self.tf_select_img_path.current.value

            if StrUtils.has_whitespace(ffmpegExec):
                temp = f"ffmpeg 路径中存在空格:{ffmpegExec}"
                print(temp)
                CommonUtils.showSnack(self.page,temp)
                return
            if StrUtils.has_whitespace(videoPath):
                temp =f"视频路径中存在空格:{videoPath}"
                print(temp)
                CommonUtils.showSnack(self.page,temp)
                return
            if StrUtils.has_whitespace(imgPath):
                temp =f"封面路径中存在空格:{imgPath}"
                print(temp)
                CommonUtils.showSnack(self.page,temp)
                return
            outputVideoPath = FileUtils.getDirAvailablePath(self.tf_select_video_path.current.value)

            FFmpegUtils.setFFmpegExecutPath(ffmpegExec)
            ress=FFmpegUtils.changeCover(videoPath,
                                    imgPath,
                                    1000, 2,
                                    outputVideoPath)
            if ress:
                CommonUtils.showSnack(self.page,f'处理成功,文件保存在:{outputVideoPath}')
            else:
                CommonUtils.showSnack(self.page,f'处理失败,未知错误')
            pass
        else:
            print("click err")
            pass

    def build(self):
        return Container(
            content=Column([
                Row([
                    TextField(ref=self.tf_select_video_path, label='视频路径'),
                    ElevatedButton(ref=self.btn_select_video_path, text='选择视频', on_click=self.btn_click)
                ]),
                Row([
                    TextField(ref=self.tf_select_img_path, label='封面路径'),
                    ElevatedButton(ref=self.btn_select_img_path, text='选择封面', on_click=self.btn_click)
                ]),
                ElevatedButton(ref=self.btn_run_ffmpeg, text='执行', on_click=self.btn_click)
            ],
                scroll=ScrollMode.ALWAYS,
                alignment=MainAxisAlignment.CENTER
            ),
            alignment=alignment.center

        )
