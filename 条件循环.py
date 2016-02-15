# _*_ coding:utf-8 _*_
print("打tests")
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
birthday = int(input('input number:'))

print(birthday)
if birthday >= 2000:
	print('00hou')
elif birthday < 2000:
	print('非00hou')
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print('和是', sum)
sum = 0
for xx in range(12):
	print(xx)

