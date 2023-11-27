import 'dart:collection';

import 'package:flutter_smart_dialog/flutter_smart_dialog.dart';
import 'package:get/get.dart';
import 'package:pitcher_tool/http/http.dart';
import 'package:pitcher_tool/models/browser_debug_config.dart';
import 'package:pitcher_tool/models/facebook_msg.dart';
import 'package:pitcher_tool/utils/str_utils.dart';
import 'package:velocity_x/velocity_x.dart';

import 'index.dart';

class QuickFacebookApiController extends GetxController {
  QuickFacebookApiController();

  final state = QuickFacebookApiState();

  ///返回生成的账号id,失败则返回空
  Future<String?> createFacebookUser(String inputText,
      {String? browserName}) async {
    if (inputText.isEmpty) {
      SmartDialog.showToast("信息为空");
      return null;
    }

    FacebookMsg facebookMsg = StrUtils.getFacebookMsg(inputText);
    print(facebookMsg);
    Map? result = await HttpUtils.creatFacebookUser(
        facebookMsg: facebookMsg,
        groupId: state.selectedGroupId,
        name: browserName ?? "");
    if (result == null || result['code'] == -1) {
      return null;
    }

    return result['data']['id'];
  }

  Future<BrowserDebugConfig?> openBrowser(String id) async {
    Map? result = await HttpUtils.openBrowser(id);
    if (result == null || result['code'] == -1) {
      return null;
    }
    var data = result['data'];
    return BrowserDebugConfig(
        debugUrl: data['ws']['selenium'],
        debugPort: data['debug_port'],
        webDriver: data['webdriver']);
  }

  Future<void> queryPackets() async {
    Map? result = await HttpUtils.queryPackets();
    if (result == null || result['code'] == -1) {
      return null;
    }

    List<dynamic> data = result['data']['list'];
    print(data);
    state.facebookAccountGroup = data;
    // update();
  }

  String? getGroupName({String? groupId}) {
    groupId = groupId ?? state.selectedGroupId;

    for (var item in state.facebookAccountGroup) {
      if (groupId == item['group_id']) {
        return item['group_name'];
      }
    }
    return null;
  }

  /// 在 widget 内存中分配后立即调用。
  @override
  void onInit() {
    super.onInit();
    queryPackets();
  }

  /// 在 onInit() 之后调用 1 帧。这是进入的理想场所
  @override
  void onReady() {
    super.onReady();
  }

  /// 在 [onDelete] 方法之前调用。
  @override
  void onClose() {
    super.onClose();
  }

  /// dispose 释放内存
  @override
  void dispose() {
    super.dispose();
  }
}
