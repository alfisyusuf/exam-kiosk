from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=collect_data_files('PyQt5'),
    hiddenimports=['PyQt5.QtPrintSupport'] + collect_submodules('PyQt5'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ExamKiosk',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'  # Anda perlu menyediakan file icon.ico
)

# Khusus untuk macOS
app = BUNDLE(
    exe,
    name='ExamKiosk.app',
    icon='icon.icns',  # Anda perlu menyediakan file icon.icns
    bundle_identifier='com.examkiosk.app',
    info_plist={
        'CFBundleShortVersionString': '1.0.0',
        'LSEnvironment': {
            'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'
        }
    }
)
