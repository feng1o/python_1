# _*_ coding:utf-8 _*_


class animal(object):
    def lives(self):
        print("has alives")


class dog(animal):
    pass


class fish(object):
    def swiming(self):
        print("swinming")


class person(animal, fish):
    pass
per1 = person()
per1.swiming()
per1.lives()

# 在设计类的继承关系时，通常，主线都是单一继承下来的，
# 例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
# 通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，
# 再同时继承Runnable。这种设计通常称之为MixIn。


# __str__
class student(object):
    """docstring for  student"""

    def __init__(self, name):
        self.name = name

    @property
    def Name(self):
        print("name = %s" % self._Name)
st1 = student("lname")
print(st1.name)

print(student("st2"))  # <__main__.student object at 0x0034BDD0> 打印这个


class student(object):
    """docstring for  student"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "use __str__()：name is :%s" % self.name

print(student("st2"))  # 不会<__main__.student object at 0x0034BDD0> 打印这个

# 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用
# 户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

"""解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，
有个偷懒的写法："""


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


# __iterator__

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

for n in Fib():
    print(n)


# __getitem__

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# __getattr__

# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：


class Student(object):

    def __init__(self):
        self.name = 'Michael'


class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

s = Student()
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
print("s.score= %s" % s.score)


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


# call

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

callable(max)  # 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
