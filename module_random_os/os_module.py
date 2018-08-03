#!/bin/python
#FileName:
#author: lf
import os
import re
from subprocess import call

with os.popen('tasklist', 'r') as f:
    for eachLine in f:
    	print(eachLine)
    	# sprint(re.split('\s\s+|\t', eachLine.rstrip()))

os.system('tasklist')

'''' subprocess模块与系统模块（system）比较，subprocess模块的的优势是更加灵活。我觉得os.system模块是过时的，我觉得他应该是这样的：replacing-older-functions-with-the-subprocess-module

但是，对于快速的一次性的脚本，使用os.system就足够了

作者：路人甲
链接：https://zhuanlan.zhihu.com/p/23480275
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
call(['tasklist'])