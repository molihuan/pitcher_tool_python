import 'package:get/get.dart';

import 'controller.dart';

class QuickFacebookApiBinding implements Bindings {
  @override
  void dependencies() {
    Get.lazyPut<QuickFacebookApiController>(() => QuickFacebookApiController());
  }
}
