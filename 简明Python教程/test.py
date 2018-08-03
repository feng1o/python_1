#! /usr/bin/python
# FileName: test.py

import os
import time
import sys
import warnings
if sys.version_info[0] < 3:
	warnings.warn("need python 3...")
else:
	warnings.warn("this is python3")

dic = {}
dic['a'] = {'b':1}
print(dic['a']['b'])

print(time.strftime("%Y%M%H%M%S"))
print(os.sep)

source = "D:\\yun"

print(format(''.join(source)))

target_dir = 'c:\\'
target = target_dir +\
    time.strftime('%Y') + '年' +\
    time.strftime('%m') + '月' +\
    time.strftime('%d') + '日_' +\
    time.strftime('%H') + '时' +\
    time.strftime('%M') + '分' +\
    time.strftime('%S') + '秒' +\
    '.rar'

print(target)

source = ['"C:\\tmp"', 'C:\\temp']
# 当要备份的文件的目录名中有空格时，要用如'"C:\\program files"'形式的表示方法。

print('"d:\\sys file"')
print("d:\\sys file")

if not False:
    print("not false")
else:
    print("false")

print("x b c".replace(' ', '_'))
