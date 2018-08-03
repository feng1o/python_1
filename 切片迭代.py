# _*_ coding:utf-8 _*_
from collections import Iterable
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myList[:3:2])
print('后5个数字[-5:]=%s' % myList[-5:])

string = 'abcdefghijklmn'
print("string=%s" % string)
print("string[0:2:1]=%s" % string[:10:3])

print("跌跌带。。。。。。")
dict1 = {'liu': 1, 'feng': 2, 'hai': 3}
for key in dict1:
	print('  %30s' % key)

# from collections import Iterable
print('\nstrng是否可迭代=%s' % isinstance('abc', Iterable))
print(isinstance(123, Iterable)) # 整数是否可迭代)	

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)

for i, value in enumerate('abc'):
	print(i, value)