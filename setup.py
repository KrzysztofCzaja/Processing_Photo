import sys
from cx_Freeze import setup, Executable
import os.path

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], 'include_files':['tk86t.dll','tcl86t.dll','camera.ico','source','temp','product']}

# GUI applications require a different base on Windows (the default is for a
# console application).
os.environ['TCL_LIBRARY'] = r'c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\tcl\tk8.6'
# options = {
#     'build_exe': {
#         'include_files':[
#             os.path.join("c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64", 'DLLs', 'tk86t.dll'),
#             os.path.join("c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64", 'DLLs', 'tcl86t.dll'),
#          ],
#     },
# }
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Image Tool",
        version = "0.1",
        description = "Imqage Tooling application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("ImageTool.py", base=base)])

