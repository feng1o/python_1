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

cperson2.xxx = 'xxxxxxxxxbbbbbb'
print("cperson2.xx = %s" % cperson2.xxx)
cperson2.getName()
cperson2.bindMethodAge('xxxxxxxxxxxxxxxxxxxxx')
cperson2.getName()


# __slots__ 用tuple定义允许绑定的属性名称
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，
# 来限制该class实例能添加的属性：

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

# x1.price = 'pricexx'  # slots 里面没有price不行


# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# 比如加入判定
print("\n@property")
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
st1 = Student()
st1.set_score(80)
st1.set_score(800)  # 报错
