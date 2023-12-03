from enum import Enum


class BrowserDebugType(Enum):
    SELENIUM = "selenium"
    PLAYWRIGHT = "playwright"


class BrowserDebugConfig():
    def __init__(self, debugUrl=None, webDriver=None, debugPort=None, debugWsUrl=None,
                 browserDebugType=BrowserDebugType.SELENIUM):
        self.browserDebugType = browserDebugType
        # selenium调试需要信息
        self.debugUrl = debugUrl
        self.debugPort = debugPort
        self.webDriver = webDriver
        # playwright调试需要信息
        self.debugWsUrl = debugWsUrl

    def __str__(self):
        return f"BrowserDebugConfig(browserDebugType={self.browserDebugType}, debugUrl={self.debugUrl}, debugPort={self.debugPort}, webDriver={self.webDriver}, debugWsUrl={self.debugWsUrl})"
