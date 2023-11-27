import 'package:http_mock_adapter/http_mock_adapter.dart';
import 'package:pitcher_tool/http/http.dart';
import 'package:pitcher_tool/models/facebook_msg.dart';

import 'api.dart';

class HttpMock {
  ///配置拦截请求
  static DioAdapter dioAdapter = DioAdapter(
    dio: dio,

    ///全路径匹配
    matcher: const FullHttpRequestMatcher(),
  );

  static void init({bool need = true}) {
    if (need) {
      getAdspowerStatus();
      queryPackets();
      openBrowser();
      creatFacebookUser();
    }
  }

  static void getAdspowerStatus() {
    dioAdapter.onGet(
      URL_STATUS,
      (server) => server.reply(
        200,
        {"code": 0, "msg": "success"},
        // Reply would wait for one-sec before returning data.
        // delay: const Duration(seconds: 1),
      ),
    );
  }

  static void queryPackets() {
    dioAdapter.onGet(
      URL_QUERY_PACKETS,
      (server) => server.reply(
        200,
        {
          "code": 0,
          "data": {
            "list": [
              {
                "group_id": "100", //分组ID，添加账号时需要
                "group_name": "莫利欢" //分组名称
              },
              {"group_id": "101", "group_name": "2组"}
            ],
            "page": 1,
            "page_size": 10
          },
          "msg": "Success"
        },
        // Reply would wait for one-sec before returning data.
        // delay: const Duration(seconds: 1),
      ),
    );
  }

  ///[id]账号id
  static void openBrowser({String? id}) {
    dioAdapter.onGet(
      URL_START_BROWSER,
      (server) => server.reply(
        200,
        {
          "code": 0,
          "data": {
            "ws": {
              "selenium": "127.0.0.1:xxxx",
              //浏览器debug接口，可用于selenium自动化
              "puppeteer": "ws://127.0.0.1:xxxx/devtools/browser/xxxxxx"
              //浏览器debug接口，可用于puppeteer自动化
            },
            "debug_port": "xxxx", // debug端口
            "webdriver": "C:\\xxxx\\chromedriver.exe" // webdriver路径
          },
          "msg": "success"
        },
        // Reply would wait for one-sec before returning data.
        // delay: const Duration(seconds: 1),
      ),
    );
  }

  static void creatFacebookUser({FacebookMsg? facebookMsg}) {
    dioAdapter.onPost(
      URL_CREATE_USER,
      (server) => server.reply(
        200,
        {
          "code": 0,
          "data": {
            "id": "xxxxxxx" //账号添加成功之后的唯一ID
          },
          "msg": "Success"
        },
        // Reply would wait for one-sec before returning data.
        // delay: const Duration(seconds: 1),
      ),
    );
  }
}
