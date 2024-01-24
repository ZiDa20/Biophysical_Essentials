# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['start.py'],
    pathex=['/QT_GUI/',
    '/QT_GUI/MainWindow'],
    binaries=[],
    datas=[('./StyleFrontend', 'StyleFrontend'),
            ('./database', 'database'),
            ('./QT_GUI', 'QT_GUI'),
            ('./qbstyles', 'qbstyles'),
            ('./resources.py', '.')],
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
