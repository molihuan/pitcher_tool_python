import os
import subprocess
import platform


class FileUtils():
    @staticmethod
    def exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def getAssetsPath():
        # 获取当前工作目录的路径
        current_dir = os.getcwd()
        # TODO打包后路径
        assets_path = os.path.join(current_dir, "assets")
        return assets_path
    @staticmethod
    def getClientPath():
        # 获取当前工作目录的路径
        current_dir = os.getcwd()
        # TODO打包后路径
        assets_path = os.path.join(current_dir, "client")
        return assets_path

    @staticmethod
    def open_file_or_folder(path):
        if os.path.isfile(path):
            FileUtils.open_file_with_default_program(path)
        elif os.path.isdir(path):
            FileUtils.open_folder_with_file_manager(path)
        else:
            print("Path does not exist.")

    @staticmethod
    def open_file_with_default_program(file_path):
        system = platform.system()
        try:
            if system == 'Windows':
                subprocess.Popen(['start', file_path], shell=True)
            elif system == 'Darwin':  # macOS
                subprocess.Popen(['open', file_path])
            elif system == 'Linux':
                subprocess.Popen(['xdg-open', file_path])
            else:
                print("Unsupported operating system.")
        except FileNotFoundError:
            print("File not found.")

    @staticmethod
    def open_folder_with_file_manager(folder_path):
        system = platform.system()
        try:
            if system == 'Windows':
                subprocess.Popen(['explorer', folder_path])
            elif system == 'Darwin':  # macOS
                subprocess.Popen(['open', folder_path])
            elif system == 'Linux':
                subprocess.Popen(['xdg-open', folder_path])
            else:
                print("Unsupported operating system.")
        except FileNotFoundError:
            print("Folder not found.")
