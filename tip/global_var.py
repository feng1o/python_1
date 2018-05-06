#!/usr/bin/python
# FileName: global_var.py

import sys

g_num = 0


def fun(num):
    '''fun:

    1.测试全局变量。先声明global xxx
    2.++（--）在Python里面是不行的，不能实现自增自检，会被任务是+ —负号
    '''
    global g_num
    g_num = num
    # ++g_num  # 不能实现自增
    g_num += 1  # ok
    print("globa num = {}".format(g_num))


if __name__ == '__main__':
    fun(2)

# locals()对象的值不能修改，globals()对象的值可以修改
z = 0


def f():
    z = 1
    x = 3
    print(locals())
    locals()["z"] = 2
    print('xx', locals())
f()
globals()["z"] = 2
print(z)
print(globals())
