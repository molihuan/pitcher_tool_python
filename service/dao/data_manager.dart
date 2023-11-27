import 'dart:collection';

import 'package:excel/excel.dart';
import 'package:nb_utils/nb_utils.dart';
import 'package:pitcher_tool/models/shortcut_file_item.dart';
import 'package:pitcher_tool/utils/excel_utils.dart';

class DataManager {
  static final DataManager _instance = DataManager._internal();

  factory DataManager() {
    return _instance;
  }

  DataManager._internal(); // 私有构造函数

  set groupId(String value) {
    setValue("GroupId", value);
  }

  String get groupId {
    return getStringAsync("GroupId");
  }

  Future<List<ShortcutFileItem>> getShortcutFileConfig() async {
    List<ShortcutFileItem> btnList = [];
    Excel excel = await ExcelUtils.loadAssets('assets/ShortcutFileConfig.xlsx');
    Sheet sheet = excel["Sheet1"];

    int rowIndex = 1;
    Data btnTextData;
    Data dirFilePathData;
    while (!ExcelUtils.valueIsNull(sheet, columnIndex: 0, rowIndex: rowIndex)) {
      btnTextData = sheet
          .cell(CellIndex.indexByColumnRow(columnIndex: 0, rowIndex: rowIndex));
      dirFilePathData = sheet
          .cell(CellIndex.indexByColumnRow(columnIndex: 1, rowIndex: rowIndex));
      btnList.add(ShortcutFileItem(
          btnText: btnTextData.value.toString(),
          dirFilePath: dirFilePathData.value.toString()));
      rowIndex++;
    }
    return btnList;
  }
}
