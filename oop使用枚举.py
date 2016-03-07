# _*_ coding:utf-8 _*_

# 需要定义常量时，一个办法是用大写变量通过整数来定义
NUM = 10  # 好处是简单，缺点是类型是int，并且仍然是变量。

"""更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
Python提供了Enum类来实现这个功能："""

from enum import Enum

Month = Enum("Month", ('jan', 'feb', 'mar', 'Apr'))

for name, member in Month.__members__.items():
    # value属性则是自动赋给成员的int常量，默认从1开始计数。
    print(name, '=>', member, ',', member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum, unique


@unique     # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    xxx = 3 
for name, member in Weekday.__members__.items():
	print(name ,':',  member, member.value)
