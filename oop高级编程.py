#!/bin/bash/ env pytho3
# _*_ coding:utf-8_*_

# 使用__slots__


class Person(object):

    cType = "person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, namex):
        sefl.name = namex

    def getName(self):
        print("get Name =%s" % self.name)

cperson1 = Person('lf', 25)
cperson1.getName()


def bindMethodAge(self, name2):
    print("绑定方法设置name")
    self.name = name2
   # print("绑定方法获取年龄 = %d" % self.age)


from types import MethodType

cperson1.bindMethodAge = MethodType(bindMethodAge, cperson1)  # 给实例绑定
cperson1.bindMethodAge('ffffff')

print('Person(obj, \'age\') =', hasattr(Person, 'age'))  # 有属性'x'吗？

Person.bindMethodAge = MethodType(bindMethodAge, Person)  # 给类绑定方法
cperson2 = Person('lf', 100)
cperson2.getName()
cperson2.bindMethodAge('xxxxxxxxxxxxxxxxxxxxx')
cperson2.getName()


# __slots__ 用tuple定义允许绑定的属性名称

class xxx(object):
    """docstring for xxx"""

    __slots__ = ('name', 'age', 'ag')  # # 用tuple定义允许绑定的属性名称

    def __init__(self, ag):  # ag也必须是slot里面的
        self.ag = ag

    def print(self):
    	print("xx= %s " % self.ag)

x1 = xxx('afl')
x1.print()


x1.name = "namexxxxxxxx"

pirnt(1)

x1.price = 'pricexx'  # slots 里面没有price不行
