#!/bin/bash
# _*_ coding:utf-8 _*_

import sys

print(sys.__name__)
print(dir(sys))
print("command line arguments are:")
for i in sys.argv:
	print(i)
print("\n\nPath", sys.path, '\n')

def fun1():
    print("string....")
    print("{0} love {1}".format("I", "you"))
    print("{a} love {b}".format(a="I", b="you"))
    print('{0:.1f}{1}'.format(2.356, "GB"))
    print("%c\a" % 97)
    print("%010d" % 2)

fun1()

a = "www.baidu.com"
a = list(a)
print(a)

b = ['1', '2', '3']
print(tuple(b))
print(str(b))
print(len(b))
print(min(b))
print(max(b))

tuple1 = (1, 2, 3, 4.1)
print(sum(tuple1))
print(reversed(tuple1))
print(list(reversed(tuple1)))
print(tuple(reversed(tuple1)))

print(list(enumerate(tuple1))) 

print("\nzip")
c = [1, 2, 3, 4, 5, 6]
inde = [6, 7, 8, 9]
print(list(zip(c, inde)))

def sum(a=1, *tup, **dict):
	'''Docstring.文档字符串

	求和.'''
	count = a
	for i in tup:
		count += i
	for key in dict:
		count += dict[key]
	return count

print('\n', sum(1, 2, 3, 4, dict1 = 5, dict2 = 6))
print(sum.__doc__)  # 文档字符串