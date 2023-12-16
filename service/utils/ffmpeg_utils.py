import subprocess


class FFmpegUtils():
    _ffmpegExecutPath: str = None

    @classmethod
    def setFFmpegExecutPath(cls, v):
        cls._ffmpegExecutPath = v

    @staticmethod
    def changeCover(videoPath, imgPath, insertionCycle: float, displayFrameRate: int, outputVideoPath):
        # 毫秒转秒
        insertionCycle = insertionCycle / 1000
        # 帧数转时间(秒)1秒30帧
        displayTime = displayFrameRate / 30

        cmd = f'''{FFmpegUtils._ffmpegExecutPath} -i {videoPath} -i {imgPath} -filter_complex "[1:v]scale=-1:ih[ov];[0:v][ov]overlay=0:0:enable='lt(mod(t\,{insertionCycle}),{displayTime})'[v]" -map "[v]" -preset veryfast -c:v libx264 -pix_fmt yuv420p -movflags +faststart -map 0:a? -c:a copy {outputVideoPath}'''
        return FFmpegUtils.runCommand(cmd)

    @staticmethod
    def runCommand(cmd):
        print(cmd)

        process = subprocess.Popen(cmd, shell=True)
        process.wait()  # 等待命令执行完成
        return_code = process.returncode  # 获取命令的返回值

        if return_code == 0:
            return True
        elif return_code == 126:
            print("ffmpeg没有权限")
            return False
        else:
            return False
