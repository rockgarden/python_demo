# librarys_batch_installer.py
# 批量安装python第三方库
import os

libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", "selenium",
        "beautifulsoup4", "jieba", "wheel", "pyinstaller", "django",
        "flask", "werobot", "sympy", "pandas", "networkx",
        "pyqt5", "pyopengl", "pypdf2", "docopt", "pygame"}
try:
    for lib in libs:
        os.system("pip3 install " + lib)
    print("Successful installed ! ")
except:
    print("Failed somehow.")
