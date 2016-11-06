# -*- mode: python -*-

block_cipher = None

a = Analysis(['kombiloexe.py'],
             pathex=['C:\\Python27\\lib\\site-packages'],
             binaries=None,
             datas=[
                    (r'kombilo\lang\en\LC_MESSAGES\kombilo.mo', r'kombilo\lang\en\LC_MESSAGES'),
                    (r'kombilo\lang\de\LC_MESSAGES\kombilo.mo', r'kombilo\lang\de\LC_MESSAGES'),
                    (r'kombilo\icons\*.png', r'kombilo\icons'),
                    (r'kombilo\data\references', r'kombilo\data'),
                    (r'kombilo\default.cfg', r'kombilo'),
                    (r'kombilo\license.rst', r'kombilo'),
                    ],
             hiddenimports=['Tkinter', 'FixTk', 'Pmw', 'PmwBlt', 'PmwColor', ],
             hookspath=[],
             runtime_hooks=[],
             excludes=None,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='kombilo',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='kombilo')