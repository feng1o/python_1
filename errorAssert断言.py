# _*_ conding:utf-8 _*_

# 错误调试可以使用print,
# 或者使用断言
""" 程序中如果到处充斥着assert，、
和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert："""

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
main()

"""程序中如果到处充斥着assert，和print()相比也好不到哪去。
不过，启动python解释器时可以用-o参数来关闭assert："""

# logging 
"""把print()替换为logging是第3种方式，和assert比，
logging不会抛出错误，而且可以输出到文件："""

import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

"""logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？

别急，在import logging之后添加一行配置再试试："""

"""这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，
debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，
最后统一控制输出哪个级别的信息。"""
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# pdb
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
# $ python3 -m pdb err.py
# pbd.setting() 设置断点