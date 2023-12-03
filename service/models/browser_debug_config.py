from enum import Enum


class BrowserDebugType(Enum):
    SELENIUM = "selenium"
    PUPPETEER = "puppeteer"


class BrowserDebugConfig():
    def __init__(self, debugUrl,  webDriver,debugPort=None, browserDebugType=BrowserDebugType.SELENIUM):
        self.browserDebugType = browserDebugType
        self.debugUrl = debugUrl
        self.debugPort = debugPort
        self.webDriver = webDriver

    def __str__(self):
        return f"BrowserDebugConfig(browserDebugType={self.browserDebugType}, debugUrl={self.debugUrl}, debugPort={self.debugPort}, webDriver={self.webDriver})"
