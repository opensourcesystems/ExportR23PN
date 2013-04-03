# -*- mode: python -*-
a = Analysis(['f:\\OsSystems\\krd\\ExportR23PN\\main.py'],
             pathex=['f:\\Python26\\Lib\\site-packages', 'f:\\OsSystems\\krd\\ExportR23PN'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'main.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name=os.path.join('dist', 'main.exe.app'))
