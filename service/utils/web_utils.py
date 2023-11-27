import webbrowser


class WebUtils:
    @staticmethod
    def open_url(url: str, browser_path=None):
        """
        在Web浏览器中打开指定的网址。

        :param url: 要打开的网址。
        :param browser_path: 可选参数，指定要使用的Web浏览器路径，默认为系统默认浏览器。
        """
        if browser_path:
            return webbrowser.get(browser_path).open(url)
        else:
            return webbrowser.open(url)
