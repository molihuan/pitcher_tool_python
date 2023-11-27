import requests

# 创建一个 Session 对象，并设置基地址
from service.http.api import URL_QUERY_PACKETS, URL_START_BROWSER, URL_CREATE_USER


class HttpUtils:
    # 查询分组
    @staticmethod
    def queryPackets():
        response = requests.get(URL_QUERY_PACKETS, params={'page_size': 20})
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("queryPackets err")
            return None

    # 打开浏览器
    @staticmethod
    def openBrowser(id):
        response = requests.get(URL_START_BROWSER, params={'user_id': id})
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("openBrowser err")
            return None

    # 创建facebook账户
    @staticmethod
    def creatFacebookUser(facebookMsg, groupId, name='', ):
        payload = {
            'name': name,
            'group_id': groupId,
            'user_proxy_config': {"proxy_soft": "no_proxy"},
            'fingerprint_config': {
                "automatic_timezone": "1",
                "language": ["en-US", "en", "zh-CN", "zh"],
                "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36",
            },
            'domain_name': 'https://facebook.com',
            'open_urls': [
                'https://start.adspower.net/',
                'https://facebook.com',
                'https://outlook.com',
            ],
            'username': facebookMsg['userName'],
            'password': facebookMsg['userPwd'],
            'fakey': facebookMsg['checkCode'],
            'remark': f"{facebookMsg['email']}\n{facebookMsg['emailPwd']}\n{facebookMsg['idCardImgUrl']}",
        }
        response = requests.post(URL_CREATE_USER, json=payload)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("creatFacebookUser err")
            return None
