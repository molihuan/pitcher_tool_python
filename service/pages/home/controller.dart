import 'package:get/get.dart';
import 'package:pitcher_tool/http/mock.dart';

import 'package:pitcher_tool/pages/home/state.dart';

import 'index.dart';

class HomeController extends GetxController {
  final state = HomeState();

  Future<void> getShortcutFileConfig() async {
    state.shortcutFileList = await state.dataManager.getShortcutFileConfig();
  }

  /// 在 widget 内存中分配后立即调用。
  @override
  void onInit() {
    super.onInit();
    getShortcutFileConfig();
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
