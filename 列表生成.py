# print("....列表生成")
import os  # 导入os模块，模块的概念后面讲到

print("列表生成")
list1 = []
for x in range(1, 11):
	list1.append(x)
print(list1)

list2 = []
for x in range(1, 11):
	list2.append(x*x)
print(list2)

print([x*x for x in range(1, 16)])  # jian简单方式

print('两层循环全排列')
print([m+n for m in 'abc'  for n in 'de'])  # 两层循环全排列

# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
# import os  # 导入os模块，模块的概念后面讲到
print ([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录

d = {'a': '1', 'b': '2', 'c': '3'}
print([x +'='+ y for x, y in d.items()])

listx = ['ABC', 'DEF']
print([s.lower() for s in listx])

listy = ['ABC', 12, 'BCD', 'EFDG', None]
# print([s.lower() for s in listy])  # 错误，遇到非str了
print('简单方法:', [s.lower() for s in listy if isinstance(s, str)])


listyy = []
for s in listy:
	if isinstance(s, str):
		listyy.append(s)
print(listyy)
