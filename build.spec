# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Main.py'],  # Cambia esto al nombre de tu archivo principal
    pathex=['/Users/nasratullahjabarkhil/PycharmProjects/Desktop UI/UI'],
    binaries=[],
    datas=[('assets/*', 'assets')],
    hiddenimports=['PIL', 'tkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SenseOS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    icon='assets/logo.icns',  # Asegúrate de tener este archivo
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)