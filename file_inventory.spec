# file_inventory.spec - Windows-specific version
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['file_inventory.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'pandas', 
        'openpyxl', 
        'et_xmlfile', 
        'xlsxwriter', 
        'numpy',
        'pandas.io.formats.excel',
        'pandas.io.excel._base',
        'pandas.io.excel._openpyxl',
        'pandas.io.excel._xlsxwriter'
    ],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='file_inventory',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)