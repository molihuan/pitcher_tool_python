import sys
from enum import Enum


class SysType(Enum):
    UNKNOWN = 0
    WIN = 1
    LINUX = 2
    MAC = 3


class SysUtils():
    # 获取系统类型
    @staticmethod
    def getSysType():
        if sys.platform.startswith('win'):
            return SysType.WIN
        elif sys.platform.startswith('linux'):
            return SysType.LINUX
        elif sys.platform.startswith('darwin'):
            return SysType.MAC
        else:
            return SysType.UNKNOWN
