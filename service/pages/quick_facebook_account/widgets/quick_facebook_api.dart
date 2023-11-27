import 'package:flutter/material.dart';
import 'package:flutter_smart_dialog/flutter_smart_dialog.dart';
import 'package:get/get.dart';
import 'package:nb_utils/nb_utils.dart';
import 'package:pitcher_tool/models/facebook_msg.dart';
import 'package:pitcher_tool/utils/str_utils.dart';
import 'package:velocity_x/velocity_x.dart';

import '../index.dart';

/// hello
class QuickFacebookApi extends GetView<QuickFacebookApiController> {
  QuickFacebookApi({Key? key}) : super(key: key);
  TextEditingController textController = TextEditingController();
  TextEditingController browserNameController = TextEditingController();

  late List facebookAccountGroup = controller.state.facebookAccountGroup;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: VStack([
        Text(
          "请粘贴完整的二解信息",
          style: TextStyle(fontSize: 19),
        ).text.make().center().onTap(() {
          print(facebookAccountGroup.length);
        }),
        VxTextField(
          controller: textController,
          maxLine: 5,
          hint: "请粘贴在这里",
        ).py12().p16(),
        VStack([
          HStack([
            Obx(() => "当前分组为:${controller.getGroupName()}".text.make().px20()),
            ElevatedButton(
                onPressed: () async {
                  VxBottomSheet.bottomSheetOptions(
                    context,
                    option: [
                      for (var item in facebookAccountGroup)
                        item["group_name"] + ":" + item["group_id"] as String
                    ],
                    defaultData: 'Flutter',
                    backgroundColor: Colors.white,
                    roundedFromTop: true,
                    enableDrag: false,
                    isSafeAreaFromBottom: true,
                    onSelect: (index, value) {
                      // VxToast.show(context, msg: 'index=$index value=$value');
                      controller.state.selectedGroupId =
                          facebookAccountGroup[index]["group_id"];
                    },
                  ).then((data) {
                    Vx.log('Test data=$data');
                  });
                },
                child: "选择分组".text.make().px8()),
            // Container(
            //   child: TextField(),
            // )
          ]).px64().centered(),
          TextField(
            controller: browserNameController,
            decoration: InputDecoration(label: "浏览器名称(选填)".text.make()),
          ).px64().py16(),
          ElevatedButton(
                  onPressed: () async {
                    if (controller.state.selectedGroupId.isEmpty) {
                      SmartDialog.showToast("请先选择分组");

                      return;
                    }

                    String? browserId = await controller.createFacebookUser(
                        textController.text,
                        browserName: browserNameController.text);
                    if (browserId != null) {
                      SmartDialog.showToast("创建成功,正在为你打开,请稍后...");
                      textController.text = "";
                      controller.openBrowser(browserId);
                    } else {
                      SmartDialog.showToast("创建失败,请检查二解信息,或联系开发者");
                    }
                  },
                  child: "创建账号并打开".text.make().px64().py8())
              .centered(),
        ]).centered(),
      ]).scrollVertical(),
    );
  }
}
