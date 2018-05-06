# _*_ coding:utf-8 _*_

# 比如int（’133')会默认的变成133十进制数字，如果想改变int（‘0101010’， base=2）
# 会变成2进制转换，那么每次要输入，可以使用默认参数定义def一个函数，但还是比较麻烦，
# 引用偏函数就可以方便搞定，
# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住 
# （也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# >>> import functools
# >>> int2 = functools.partial(int, base=2)

import functools
print(int('12323'))
print(int('10011111', base=2))

intn = functools.partial(int, base=2)
print(intn('111101'))
print(intn('111101', base=10))

xx = put()