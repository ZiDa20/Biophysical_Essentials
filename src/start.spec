# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['start.py'],
    pathex=['/Users/maximilianzeidler/Desktop/Biophysical_Essentials/src/QT_GUI/',
    '/Users/maximilianzeidler/Desktop/Biophysical_Essentials/src/QT_GUI/MainWindow',
    '/Users/maximilianzeidler/Desktop/Biophysical_Essentials/src/'],
    binaries=[],
    datas=[('/Users/maximilianzeidler/Desktop/Biophysical_Essentials/src/StyleFrontend', 'StyleFrontend'),
            ('/Users/maximilianzeidler/Desktop/Biophysical_Essentials/src/database', 'database'),
            ('/Users/maximilianzeidler/Desktop/Biophysical_Essentials/src/QT_GUI', 'QT_GUI'),
            ('/Users/maximilianzeidler/Desktop/Biophysical_Essentials/src/qbstyles', 'qbstyles'),
            ('/Users/maximilianzeidler/Desktop/Biophysical_Essentials/src/resources.py', '.')],
    hiddenimports=['QT_GUI',
                    'QT_GUI.MainWindow',
                    'qbstyles'],
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
    name='start',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='start',
)