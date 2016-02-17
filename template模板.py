# !/bin/bash/env python3  # 保证能在Unix上跑
#_*_ coding:utf-8 _*_

'my template'   # 模板的第一个字符串认为是注释
_author_ = 'lf'

import sys  # 导入sys模块后,利用sys这个变量，就可以访问sys模块的所有功能。


def test():
    argstr = sys.argv
    if len(argstr) == 1:
        print("没有输入参数!")
    elif len(argstr) == 2:
        print('Hello, %s!' % argstr[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':  # 当我们在命令行运行hello模块文件时，
							# Python解释器把一个特殊变量__name__置为__main__，
							# 而如果在其他地方导入该hello模块时，if判断将失败，
							# 因此，这种if测试可以让一个模块通过命令行运行时执行
							# 一些额外的代码，最常见的就是运行测试。
    test() 


# 作用域


def _privateFun1(name):
    return "namexxxx= %s" % name


def _privateFun2(name):
    return "namlen2==%s" % name

def publicFun(name):
    if len(name) >= 2:
        return _privateFun2(name)
    else:
        return _privateFun1(name)

