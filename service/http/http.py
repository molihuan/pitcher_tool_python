import json

import requests

from service.http.api import URL_QUERY_PACKETS, URL_START_BROWSER, URL_CREATE_USER, URL_STATUS, URL_STOP_BROWSER, \
    URL_ACTIVE_BROWSER, URL_ACCOUNT_LIST
from service.models.facebook_account_msg import FacebookAccountMsg


class HttpUtils:
    _debug: bool = False

    @classmethod
    def setDebug(cls, v):
        cls._debug = v

    @staticmethod
    def getApiStatus():
        if HttpUtils._debug:
            json_str = '''
            {
              "code":0,
              "msg":"success"
            }
            '''
            # 解析JSON字符串
            json_obj = json.loads(json_str)
            return json_obj
        response = requests.get(URL_STATUS)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("getApiStatus err")
            return None

    # 查询分组
    @staticmethod
    def queryPackets():
        if HttpUtils._debug:
            json_str = '''
            {
                "code": 0,
                "data": {
                  "list": [
                    {
                      "group_id": "1",     
                      "group_name": "group1"  
                    },
                    {
                      "group_id": "2",
                      "group_name": "group2"
                    }
                  ],
                  "page": 1,
                  "page_size": 10
                },
                "msg": "Success"
            }
            '''
            # 解析JSON字符串
            json_obj = json.loads(json_str)
            return json_obj

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
        if HttpUtils._debug:
            json_str = '''
            {
              "code":0,
              "data":{
                "ws":{
                  "selenium":"127.0.0.1:xxxx",    
                  "puppeteer":"ws://127.0.0.1:xxxx/devtools/browser/xxxxxx"   
                },
                "debug_port": "xxxx", 
                "webdriver": "C:/xxxx/chromedriver.exe" 
              },
              "msg":"success"
            }
            '''
            # 解析JSON字符串
            json_obj = json.loads(json_str)
            return json_obj
        response = requests.get(URL_START_BROWSER, params={'user_id': id})
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("openBrowser err")
            return None

    # 关闭浏览器
    @staticmethod
    def closeBrowser(id):
        if HttpUtils._debug:
            json_str = '''
            {
              "code":0,
              "data":{},
              "msg":"success"
            }
            '''
            # 解析JSON字符串
            json_obj = json.loads(json_str)
            return json_obj
        response = requests.get(URL_STOP_BROWSER, params={'user_id': id})
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("closeBrowser err")
            return None

    # 启动状态
    @staticmethod
    def startupStatus(id):
        if HttpUtils._debug:
            # 浏览器已打开运行中 "Active" ，未打开则是 "Inactive"
            # 浏览器debug接口，可用于selenium自动化
            # 浏览器debug接口，可用于puppeteer自动化
            json_str = '''
                {
                  "code":0,
                  "data":{
                    "status": "Active",   
                    "ws":{
                      "selenium":"127.0.0.1:xxxx",
                      "puppeteer":"ws://127.0.0.1:xxxx/devtools/browser/xxxxxx"
                    }
                  },
                  "msg":"success"
                }
            '''
            # 解析JSON字符串
            json_obj = json.loads(json_str)
            return json_obj
        response = requests.get(URL_ACTIVE_BROWSER, params={'user_id': id})
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("closeBrowser err")
            return None

    # 创建facebook账户
    @staticmethod
    def creatFacebookUser(facebookMsg: FacebookAccountMsg, groupId, name='', ):
        if HttpUtils._debug:
            json_str = '''
                {
                  "code": 0,
                  "data": {
                    "id":"xxxxxxx"
                  },
                  "msg": "Success"
                }
            '''
            # 解析JSON字符串
            json_obj = json.loads(json_str)
            return json_obj
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
            ],
            'username': facebookMsg.userName,
            'password': facebookMsg.userPwd,
            'fakey': facebookMsg.checkCode,
            'remark': f"{facebookMsg.email}\n{facebookMsg.emailPwd}\n{facebookMsg.idCardImgUrl}",
        }
        response = requests.post(URL_CREATE_USER, json=payload)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("creatFacebookUser err")
            return None

    @staticmethod
    def getAccountList(group_id: str, page: int):
        if HttpUtils._debug:
            json_str = '''
                {
                  "code": 0,
                  "data": {
                    "list": [
                    {
                      "serial_number": "1",
                      "user_id": "1",
                      "name": "username1",
                      "group_id": "1",
                      "group_name": "XX",
                      "domain_name": "facebook.com",
                      "username": "121121151245121",
                      "remark": "remark1",
                      "sys_app_cate_id": "X",
                      "created_time": "1612520997",
                      "ip": "13.251.172.174",
                      "ip_country": "sg",
                      "password": "",
                      "last_open_time": "1621333030"
                    },{
                      "serial_number": "2",
                      "user_id": "2",
                      "name": "username2",
                      "group_id": "1",
                      "group_name": "XX",
                      "domain_name": "facebook.com",
                      "username": "1245254254",
                      "remark": "remark2",
                      "sys_app_cate_id": "X",
                      "created_time": "1612520998",
                      "ip": "13.251.172.174",
                      "ip_country": "sg",
                      "password": "",
                      "last_open_time": "1621333031"
                    }],
                    "page": 1,
                    "page_size": 6
                  },
                  "msg": "Success"
                }
            '''
            # 解析JSON字符串
            json_obj = json.loads(json_str)
            return json_obj

        response = requests.get(URL_ACCOUNT_LIST, params={'page_size': 6, 'group_id': group_id, 'page': page})
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("getAccountList err")
            return None
        pass
