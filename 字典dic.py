# _*_ coding:utf-8 _*_
dict1 = {'大米': 4, (223,'lag'): tuple, '小麦': 2, 'apple': 6.8}
for x in dict1:
    print(x)
    print(dict1[x])

# 判定key在不在里面
print("liufeng刘峰。。。")
tmp = dict1.get('liufeng', 1)
print(tmp)
print('判定在不在in:', 'liufeng' in dict1)
print('判定在不在in:', 'liufeng' not in dict1)
# print('判定在不在in:', dict1.has_key('apple'))

dict1['liufeng'] = 'lf'  # 追加
for x in dict1:
    print(x)
    print(dict1[x])

dict1.pop('apple')
for x in dict1:
    print(x)
    print(dict1[x])
