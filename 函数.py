# _*_ coding:utf-8 _*_
import math

print(max(1, 2, 3, 4, 5, 100))
print(int(12.0))


def my_fun(x):
    if x > 0:
        print(x)
    else:
        print(-x)

my_fun(20)


def my_fun2(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad type")
    if x > 0:
        print(x)
    else:
        print(-x)
my_fun2(2)


def passTest():
    pass  # pass不可少，


# 返回了两个值，实际是一个，元组而已
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(1, 2, 100, math.pi / 6)
print(x, y)

tuple = move(1, 2, 100, math.pi / 6)
print(tuple)


# 默认参数
def myPow(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print('mypow:', myPow(2))


def arguments(x, y, name="liufeng", age=23):
    print('arg1=', x)
    print('arg2=', y)
    print('name=', name)
    print('age=', age)
    return
arguments(1, 2)
arguments(1, 2, 'xx', age=100)  # 这个可以指定，不按顺序


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def addlist(list=[]):
    list.append('end')
    return list
print(addlist())
print(addlist())  # 这里的记录了两个end，，，


# 解决
def addlist2(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
print('addlist2=', addlist2())
print('addlist2=', addlist2())


# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
def changeArgument(*numbers):
    s = 0
    for x in numbers:
        s = s + x * x
    return s
print('\n可变参数', changeArgument(1, 2, 3))


# 关键字参数
def keyWord(name, age, **key):
    print('关键字参数:name=%', name, ' aeg=', age, ' key=', key)
keyWord('张三', 20)
keyWord('张三', 20, 李斯=22, 王五=25)  # 不可有''
keyWord('张三', 20, lisi=0)

dic = {'lf': 1, 'aaa': 2}
keyWord('张三', 20, 李斯=dic['lf'])
keyWord('张三', 20, **dic)


# 命名关键字和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
# *后面的参数被视为命名关键字参数。
print('\n命名关键字')


def keyWord(name, age, *, city, academic, married):
    print('关键字参数:name=%', name, ' aeg=', age, ' key=', city, academic, married)
keyWord('张三', 20, city=dic['lf'], academic='college', married='married\n')
# keyWord('张三', 20, academic=dic['lf'])  # 命名关键字必须全部写


# 关键字组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2, 3, 'a', 'b', x=99, y='liu\n')
f2(1, 2, d=99, ext=None)
f2(1, 2, d=99, ext=None)

f1(1, 2, 3, (1, 2, 3), {'liu': 1, "feng": 2})
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)  # 元组，字典直接传递过来了，，，，*，**

# 递归调用


def recurfun(n):
    if n == 1:
        return 1
    return n * recurfun(n - 1)
print('\nrecurfun(%d)=%d\n' % (5, recurfun(5)))
