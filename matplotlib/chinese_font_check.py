# -*- coding: utf-8 -*-
# File Name: chinese_font_check.py

# osx系统无fc-list 需要安装X11来解决这一问题：https://www.xquartz.org

"""
中文显示
  1. osx/linux, 运行 chinese_font_check, 确定 matplotlib 支持的中文
  2. osx: copy 相应的 ttf 到 /Users/wangkan/Library/Python/3.6/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf
  3. 修改 matplotlibrc 在 #font.family : sans-serif 对应的行增加 #font.sans-serif : Arial Unicode MS (ttf 字体对应的全名)
"""

# TODO: 自动 copy ttf 并修改 matplotlibrc 文件

import subprocess as sp  # 标准库中，调用外部程序的库，可以fork一个子进程

from matplotlib.font_manager import fontManager as fm

a = sorted([f.name for f in fm.ttflist])

for i in a:
    print(i)

mpl_fonts = set(f.name for f in fm.ttflist)

print('all font list get from matplotlib.font_manager:')
for f in sorted(mpl_fonts):
    print('\t' + f)

output = sp.check_output('fc-list :lang=zh -f "%{family}\n"',
                         shell=True, encoding="utf8")

zh_fonts = set(f.split(',', 1)[0] for f in output.split('\n'))

print('\n' + 'Chinese font list get from fc-list:')
for f in sorted(zh_fonts):
    print('\t' + f)

print('\n' + 'the fonts we can use:')
available = set(mpl_fonts) & set(zh_fonts)
for f in available:
    print('\t' + f)
