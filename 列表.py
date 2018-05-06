# -*- coding: utf-8 -*-

print(max_int)
def xx(b):
	b += 1
def x():
	a = 1
	xx(a)
	print(a)
x()
print("list刘峰")
clusterInfo = ['li', '张思', '王五']
print(clusterInfo)

print('\n直接索引列表值类似数组a[n]')
print(clusterInfo[0])
print('-1last最后一个 = %s\n' % clusterInfo[-1])

print('追加list append\n')
clusterInfo.append('Adam')
clusterInfo.insert(1, 'Jack')  # 插入指定位置
print('%s\n' % clusterInfo)

print('删除pop=%s' % clusterInfo.pop())
print('删除pop(i)=%s\n' % clusterInfo.pop(2))

print('替换a[i]=\n')
clusterInfo[1] = 22

sublist = [1, 2, 3]
clusterInfo.insert(2, sublist)
print('列表%s长度是%%\d len= %d\n' % (clusterInfo, len(clusterInfo)))
print('二维list打印 clusterInfo[2][2] = %d' % clusterInfo[2][2])  # 二维数组的问题注意

for i in clusterInfo:
    print(i)

print('''liu 
 ... feng''')

print(r'\t')  # r取消里面的专职\
