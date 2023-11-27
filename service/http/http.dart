import 'package:dio/dio.dart';
import 'package:flutter_smart_dialog/flutter_smart_dialog.dart';
import 'package:nb_utils/nb_utils.dart';
import 'package:pitcher_tool/http/api.dart';
import 'package:pitcher_tool/models/facebook_msg.dart';

final options = BaseOptions(
  baseUrl: URL_BASE_AD_API,
  connectTimeout: Duration(seconds: 5),
  receiveTimeout: Duration(seconds: 3),
);
final dio = Dio(options);

class HttpUtils {
  /////执行成功
  // {
  // "code": 0,
  // "data": {
  //   "list": [
  //     {
  //       "group_id": "100",     //分组ID，添加账号时需要
  //       "group_name": "group1"  //分组名称
  //     },
  //     {
  //       "group_id": "101",
  //       "group_name": "group2"
  //     }
  //   ],
  //   "page": 1,
  //   "page_size": 10
  // },
  // "msg": "Success"
  // }
  //
  // //执行失败
  // {
  // "code":-1,
  // "data":{},
  // "msg":"failed"
  // }
  static Future<Map?> queryPackets() async {
    Response response =
        await dio.get(URL_QUERY_PACKETS, queryParameters: {'page_size': 20});
    log(response.data);
    if (response.statusCode == 200) {
      return response.data;
    } else {
      SmartDialog.showToast("queryPackets err");
      return null;
    }
  }

  ///打开浏览器,返回调试的信息,自动化必备信息
  /////执行成功
  // {
  //   "code":0,
  //   "data":{
  //     "ws":{
  //       "selenium":"127.0.0.1:xxxx",    //浏览器debug接口，可用于selenium自动化
  //       "puppeteer":"ws://127.0.0.1:xxxx/devtools/browser/xxxxxx"   //浏览器debug接口，可用于puppeteer自动化
  //     },
  //     "debug_port": "xxxx", // debug端口
  //     "webdriver": "C:\\xxxx\\chromedriver.exe" // webdriver路径
  //   },
  //   "msg":"success"
  // }
  //
  // //执行失败
  // {
  //   "code":-1,
  //   "data":{},
  //   "msg":"failed"
  // }
  static Future<Map?> openBrowser(String id) async {
    Response response =
        await dio.get(URL_START_BROWSER, queryParameters: {'user_id': id});

    log(response.data);
    if (response.statusCode == 200) {
      return response.data;
    } else {
      SmartDialog.showToast("openBrowser err");
      return null;
    }
  }

  ///创建facebook账号
  /////执行成功
  // {
  //   "code": 0,
  //   "data": {
  //     "id":"xxxxxxx"  //账号添加成功之后的唯一ID
  //   }
  //   "msg": "Success"
  // }
  //
  // //执行失败
  // {
  //   "code":-1,
  //   "data":{},
  //   "msg":"failed"
  // }
  static Future<Map?> creatFacebookUser(
      {required FacebookMsg facebookMsg,
      String name = '',
      required String groupId}) async {
    Response response = await dio.post(URL_CREATE_USER, data: {
      'name': name,

      ///分组
      'group_id': groupId,

      ///代理设置
      'user_proxy_config': {"proxy_soft": "no_proxy"},
      'fingerprint_config': {
        "automatic_timezone": "1",
        "language": ["en-US", "en", "zh-CN", "zh"],
        "ua":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36",
      },

      ///打开域名
      'domain_name': 'https://facebook.com',
      'open_urls': [
        'https://start.adspower.net/',
        'https://facebook.com',
        'https://outlook.com',
      ],

      ///账号信息
      'username': facebookMsg.userName,
      'password': facebookMsg.userPwd,
      'fakey': facebookMsg.checkCode,
      'remark':
          '${facebookMsg.email}\n${facebookMsg.emailPwd}\n${facebookMsg.idCardImgUrl}',
    });
    log(response.data);
    if (response.statusCode == 200) {
      return response.data;
    } else {
      SmartDialog.showToast("creatFacebookUser err");
      return null;
    }
  }
}
