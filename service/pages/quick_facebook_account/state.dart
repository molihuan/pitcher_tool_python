import 'dart:collection';

import 'package:get/get.dart';
import 'package:pitcher_tool/dao/data_manager.dart';

class QuickFacebookApiState {
  // title
  final DataManager dataManager = DataManager();

  final _facebookAccountGroup = [].obs;

  set facebookAccountGroup(value) => _facebookAccountGroup.value = value;

  List get facebookAccountGroup => _facebookAccountGroup;

  ///选择的分组id
  late final _selectedGroupId = dataManager.groupId.obs;

  set selectedGroupId(value) {
    _selectedGroupId.value = value;
    dataManager.groupId = value;
  }

  String get selectedGroupId => _selectedGroupId.value;
}
