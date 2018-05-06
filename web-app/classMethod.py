#!/bin/bash env python3
#_*_ coding:utf-8 _*_

from types import MethodType

'''类绑定方法，实例加方法属性'''


class Cperson(object):
    """docstring for Cperson"""

    def __init__(self, name, age):
        super(Cperson, self).__init__()
        self.name = name
        self.age = age

    def printInfo(self):
        print('名字={0}  age={1}'.format(self.name, self.age))

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


p1 = Cperson('lf', '100')
p1.grade = '一年级'  # 给实例绑定属性
p1.printInfo()
print(p1.grade)
print()


def set_grade(self, grade):
    self.grade = grade

# p1.set_grade = MethodType(set_grade, p1)
Cperson.set_grade = MethodType(set_grade, Cperson)
p1.set_grade('6年级')
print(p1.grade)
print()

# property  和setter getter


class Cperson2(object):
    @property
    def age(self):
        return self._age   # 这个age和名字必须不一样，否则会无穷地柜

    @age.setter
    def age(self, ages):
        self._age = ages

p2 = Cperson2()
p2.age = 33
print(p2.age)
