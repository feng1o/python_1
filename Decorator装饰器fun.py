#_*_ coding: utf-8 _*_


def now1():
    pass
f = now1
print(now1.__name__)  # 函数对象有一个__name__属性，可以拿到函数的名字：
print(f.__name__)  # 函数对象有一个__name__属性，可以拿到函数的名字：

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，在代码运行期间动态增加功能的方式，“装饰器”（Decorator）。


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)  # 返回一个函数
    return wrapper  # 返货一个函数


@log  # 借助Python的@语法，相当于执行了语句：now = log(now)
def now():
    print('2015-3-25')
f2 = now
print(f2())


# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()
# 函数中返回的wrapper()函数。

# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')
print(now())  # 和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)

# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到
#wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
# 所以，一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator