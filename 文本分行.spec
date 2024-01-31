# -*- mode: python ; coding: utf-8 -*-


a = Analysis(['文本分行.py'],
             pathex=['D:\\Java\\跨境贸易\\pythonProject'],
             binaries=[],
             datas=[],
             hiddenimports=[
                 'PyQt5',
                 'PyQt5.QtCore',
                 'PyQt5.QtGui',
                 'PyQt5.QtWidgets'
             ],
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
    a.binaries,
    a.datas,
    [],
    name='文本分行',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
