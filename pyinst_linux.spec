# -*- mode: python -*-
a = Analysis(['MainWindow.py'],
             pathex=['/home/eric/pyCharGen'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'pyCharGen'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
