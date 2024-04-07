# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['start.py'],
    pathex=[],
    binaries=[],
    datas=[('./Logging', 'Logging'), ('./StyleFrontend', 'StyleFrontend'), ('./database', 'database'), ('./QT_GUI', 'QT_GUI'), ('./qbstyles', 'qbstyles'), ('./resources.py', '.')],
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
    name='BiophysicalEssentials',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Frontend\\Button\\light_mode\\offline_analysis\\bpe_logo_small.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BiophysicalEssentials',
)
