class BrowserDebugConfig {
  BrowserDebugConfig(
      {this.browserDebugType = BrowserDebugType.selenium,
      required this.debugUrl,
      required this.debugPort,
      required this.webDriver});

  BrowserDebugType browserDebugType;
  String debugUrl;
  String debugPort;
  String webDriver;
}

enum BrowserDebugType {
  selenium,
  puppeteer,
}
