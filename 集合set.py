# _*_ coding:utf-8 _*_
set1 = set([1, 2, 3, (123, 23), 4, 4, 5, 6, 7, 8, 9, 10])
for x in set1:
	print('.', x)
print('add加入元素........')
set1.add(0)
for x in set1:
	print('...', x)

set1.remove((123, 23))
print('remove删除........')
for x in set1:
	print('---', x)
