# _*_ coding:utf-8 _*_
from functools import reduce
f = abs
print(f(-10))


# 传入函数
def fun(x, y, f):
    return(f(x) + f(y))
ans = fun(-1, -9, abs)  # 传入了abs给f
print(ans)


# map 。。。。。。。。。。。。。。
def fxx(x):
    return x * x
iterator1 = map(fxx, [1, 2, 3, 4, 5, 6])  # map()传入的第一个参数是f，即函数对象本身。
                                          # 由于结果r是一个Iterator，Iterator是惰性序列，
                                          # 因此通过list()函数让它把整个序列都计算出来并返
                                          # 回一个list。
mylist = list(iterator1)
print(mylist)

# map把数字编程字符
print(list(map(str, [1, 2, 3, 4, 5])))


# reduce。。。。。。。。。。。。。。。。。。。。。
print("reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)")
# from functools import reduce


def fun2(x, y):
    return x + y
ans2 = reduce(fun2, [1, 3, 5, 7])
print(ans2)


def fun3(x, y):
    return x * 10 + y
ans3 = reduce(fun3, [1, 3, 5, 7])
print(ans3)


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
ans4 = reduce(fun3, map(char2num, '12345'))
print(ans4)


def str2int(s):  # 整理成了一个str到int的函数，，，，，
    def fun3(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fun3, map(char2num, s))
print(str2int('1234567'))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA',
# 'barT']，输出：['Adam', 'Lisa', 'Bart']：


# filter
def isOdd(x):
    return x % 2
print('filter是不是一个奇数%s' % list(filter(isOdd, [1, 2, 3, 4, 5])))


def deleteNoneChar(s):
    return s and s.strip()
print('filter删除一个空字符串%s' %
      list(filter(deleteNoneChar, ['', 'liufeng', None, 'asdkgn'])))


# sorted 排序
print('\nsorted 排序%s' % sorted([1, 3, 252, -23, -22, 13]))
print('\nsorted 排序%s' % sorted([1, 3, 252, -23, -22, 13], key=abs))
print('\nsorted 排序%s' %
      sorted([1, 3, 252, -23, -22, 13], key=abs, reverse=True))
print('\nsorted 排序%s' % sorted(['ab', 'bdab', 'ABFD', 'EBAD', 'iingdang']))
print('\nsorted 排序%s' %
      sorted(['ab', 'bdab', 'ABFD', 'EBAD', 'iingdang'], key=str.lower))
