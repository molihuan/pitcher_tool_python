import 'package:get/get.dart';
import 'package:pitcher_tool/dao/data_manager.dart';
import 'package:pitcher_tool/models/shortcut_file_item.dart';

class HomeState {
  final DataManager dataManager = DataManager();

  final _shortcutFileList = <ShortcutFileItem>[].obs;

  set shortcutFileList(value) => _shortcutFileList.value = value;

  List<ShortcutFileItem> get shortcutFileList => _shortcutFileList;
}
