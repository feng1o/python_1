# -*- coding: utf-8 -*-

ou = []
ji = []
ls = [0,1,2,3]
for i in range(0,len(ls)):
	print (i)
for i in range(1, len(ls)):
	if i % 2 == 0: 
		ou.append(i) 
	else: 
		ji.append(i)

print(ji)
print(ou)

print("list刘峰")
classmates = ['li', '张思', '王五']
print(classmates)

print('\n直接索引列表值类似数组a[n]')
print(classmates[0])
print('-1last最后一个 = %s\n' % classmates[-1])

print('追加list append\n')
classmates.append('Adam')
classmates.insert(1, 'Jack')  # 插入指定位置
print('%s\n' % classmates)

print('删除pop=%s' % classmates.pop())
print('删除pop(i)=%s\n' % classmates.pop(2))

print('替换a[i]=\n')
classmates[1] = 22

sublist = [1, 2, 3]
classmates.insert(2, sublist)
print('列表%s长度是%%\d len= %d\n' % (classmates, len(classmates)))
print('二维list打印 classmates[2][2] = %d' % classmates[2][2])  # 二维数组的问题注意

for i in classmates:
    print(i)

print('''liu 
 ... feng''')

print(r'\t')  # r取消里面的专职\
