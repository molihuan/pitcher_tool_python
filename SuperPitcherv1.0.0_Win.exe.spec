# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['E:\\software\\python\\Project\\pitcher_tool_python\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('E:\\software\\python\\Project\\pitcher_tool_python\\assets', './assets'), ('E:\\software\\python\\Project\\pitcher_tool_python\\client', './client')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SuperPitcherv1.0.0_Win.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['E:\\software\\python\\Project\\pitcher_tool_python\\assets\\imgs\\ml.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SuperPitcherv1.0.0_Win.exe',
)
