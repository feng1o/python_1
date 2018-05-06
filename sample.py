#_*_ coding:utf-8 _*_

import random

a = {random.randint(1,100), random.randint(1,100)};
print(len(a))
print(a)
lst = []
for x in a:
	lst.append(x)

print("before lst = ", lst)

if lst[0] > lst[1]:
	tmp = lst[0]
	lst[0] = lst[1]
	lst[1] = tmp

print("sorted lst = ", lst)

mailto = ['cc', 'bbbb', 'afa', 'sss', 'bbbb', 'cc', 'shafa']
addr_to = list(set(mailto))
addr_to.sort(key = mailto.index)
print(set(mailto))
print(addr_to)

print(list(set(mailto)))