# import tupple
# _*_ coding:utf-8 _*_
tuple = (1, 2, 3, 4, 5)
print(tuple)
print(tuple[1])
print(tuple[:5])

typeName = type(tuple)
print(typeName)

tuple2 = (1)
typeName2 = type(tuple2)
print(typeName2)

tuple3 = (1,)  # 加个,号才是元组 tuple=()，也是元组，不用，
typeName3 = type(tuple3)
print(typeName3)


n = 8 * (8,)  # 8个8
print(n)

# 拼接
tuple = tuple[:2] + ("liufegn",) + tuple[2:]
print(tuple)


print('\n.....................')
liebiao = {11, 22, 33, 44, 55}  # set
print(liebiao)
typeName4 = type(liebiao)



