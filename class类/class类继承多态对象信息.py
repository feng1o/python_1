#！/bin/bash env python3
# _*_ coding:utf-8 _*_

'class'
_author_ = "lf"
import sys

print ("版本 + " ,sys.version)
class Person(object):  # 继承自object
    pass

person = Person()
person.name = "lf"  # 自由地给一个实例变量绑定属性
print("person name = %s" % person.name)

# 数据封装
class Person(object):
    """docstring for Person"""

    def __init__(self, name, age):  # 第一个self必须的，指向创建的实例本身
        self.name = name
        self.age = age

    def print(self):
        print("self.name = %s" % self.name)
        print("self.age = %d" % self.age)

person1 = Person('lf', 25)
setattr(person1, 'age', 1000000)                 # 可一个通过setattr改变属性
person1.print()


# 访问和限制

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问，

# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
# 是 特殊变量，特殊变量是可以直接访问的，不是private变量，所以
# 不能用__name__、__score__这样的变量名。


class Person(object):
    """docstring for Person"""

    def __init__(self, name, age):  # 第一个self必须的，指向创建的实例本身
        self.__name = name  # 外部就无法访问了，，，想访问就加方法，，
        self.__age = age

    def print(self):
        print("%11s.name = %s..age =%s" % (self, self.__name, self.__age))

    def getName(self):
        return self.__name

        def getAge(self):
            return self.__age  # 如果外部代码要获取name和score怎么办？
                               # 可以给Student类增加get_name和get_score这样的方法：

    def setAge(self, agex):
        self.__age = agex

person1 = Person('lf', 25)
person1.print()
print(person1.getName())
person1.setAge(1000)
person1.print()

# print(Person1.__age)  # 无法访问了

# 继承多态


class SuperPerson(Person):   # 继承自person
    pass
superson = SuperPerson('sulf', 111)
superson.print()

# 多态性


def duoTai(person1):
    person1.print()
# print("多态性%s" %s person1.name)  # name是private的无法获取
duoTai(SuperPerson("xxx", 222))


"""获取对象信息 type  types  使用isinstance()  使用dir() attr"""

import types


def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


# 使用isinstance()
print(isinstance("abd", list))
print(type('abc'))
print(isinstance('abc', str))
print(isinstance(person1, Person))
print(isinstance([1, 3, 4], (list, tuple)))

# 使用dir()  使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('abc'))
print(len('abc'))


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)  # 获取属性'y'

# 获取属性'z'，如果不存在，返回默认值404
print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))

f = getattr(obj, 'power')  # 获取属性'power'
print(f)
print(f())

"""小结
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
sum = obj.x + obj.y
就不要写：
sum = getattr(obj, 'x') + getattr(obj, 'y')
一个正确的用法的例子如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，
则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，
它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，
就不影响读取图像的功能。..."""


""" 实例属性和类属性  

由于Python是动态语言，根据类创建的实例可以任意绑定属性。 """


class Car(object):

    target = "transportion"  
    num = 0
    # 直接在class中定义属性，这种属性是类属性

    def __init__(self, target, price, lunzi):
        super(Car, self).__init__()
        self.price = price
        self.lunzi = lunzi
        self.target = target

    def print(self):
        if self.num == 0:
            self.target = "abcdd"
        print("car.target = %s lunzi=%s, price=%s" %
              (self.target, self.lunzi, self.price))
        print("car.target = {}".format(Car.target))

mycar = Car("xxxx", 66666, 4)
mycar.print()
del mycar.target 
mycar.print()
print("end")
