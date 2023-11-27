import 'dart:io';
import 'package:flutter/services.dart';
import 'package:flutter_smart_dialog/flutter_smart_dialog.dart';
import 'package:path/path.dart' as path;
import 'package:pitcher_tool/utils/platform_utils.dart';
import 'package:url_launcher/url_launcher.dart';

class FileUtils {
  static void openDirFile(String filePath) async {
    final Uri targetUrl = Uri.parse("file:$filePath");

    if (await canLaunchUrl(targetUrl)) {
      await launchUrl(targetUrl);
    } else {
      SmartDialog.showToast('不能打开： $filePath');
    }
  }

  static String? getAssetsPath() {
    var executablePath = getExecutablePath();
    return PlatformUtils.callback<String?, String? Function()>(windows: () {
      return path.join(executablePath!, "data", "flutter_assets", "assets");
    }, other: () {
      return null;
    });
  }

  static String? getExecutablePath() {
    try {
      return path.dirname(Platform.resolvedExecutable);
    } catch (e) {
      print('Failed to get current app path: $e');
      return null;
    }
  }

  static void openAssetFile(String assetPath) async {
    final bytes = await rootBundle.load(assetPath);
  }

  static String getCurrentExecutablePath() {
    return path.dirname(Platform.resolvedExecutable);
  }

  static bool exists({String? filePath, File? file}) {
    file = file ?? File(filePath!);
    return file.existsSync();
  }
}
