# _*_ coding:utf-8 _*_
print("生成器generator")

list1 = [s for s in range(1, 10)]
print(list1)

list2 = (x for x in range(1, 10))  # genertor（0)
print(list2)
print('liufeng', next(list2))  # next会记录这个iteration
for n in list2:
    print(n)

for n in range(1, 1):
    print(next(list2))  # StopIteration会超过


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(2)


print("yield生成生成器")
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# generator和函数的执行流程不一样。函数是顺序执行，
# 遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回
# 的yield语句处继续执行


def fun():
    print('step 1')
    yield(1)
    print('step 2')
    yield(2)
    print('step 3')
    yield(3)
a = fun()
print(a)  # <generator object fun at 0x006B32D0>
print(next(a))
print(next(a))
print(next(a))
#print(next(a))


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n = n + 1
   # return 'done'
for i in fib2(20):
    print("fib = {}".format(i))

# g = fib2(6)
# while True:
# 	try:
# 		x = next(g)
#         print('g:', x)
#    except StopIteration as e:
#     	print('Generator return value:', e.value)
#         break


def triangles1():
    yield [1]
    L = s = [1, 1]
    while True:
        k = n - 1
        L = [1, 1]
        e = 1
        while k:
            L.insert(e, s[e] + s[e - 1])
            k = k - 1
            e = e + 1
        s = L
        yield L      
for tt in triangles1():
	print(tt)
	n = n + 1
	if n==10:
		break

print("............")
def triangles():
    bb = [1]
    while True:
        yield bb
        bb = [1] + [bb[i] + bb[i + 1] for i in range(len(bb) - 1)] + [1]
