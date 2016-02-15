# 返回函数
# _*_ coding  :utf-8 _*_


def returnFun(*arg):
    def fun1():
        s = 0
        for n in arg:
            s = s + n
        return s
    return fun1  # 返回的并不是求和结果，而是求和函数：
fun = returnFun(1, 2, 3, 4, 5, 6)  # 返回的并不是求和结果，而是求和函数：
print(fun())

fun = returnFun(1, 2, 3, 4, 5, 6)  # i闭包，结果不影响，两个不同的数：
print(fun())

# 闭包 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())  # 都是一样的，原因就在于返回的函数引用了变量i，
                         # 但它并非立刻执行。等到3个函数都返回时，
                         # 它们所引用的变量i已经变成了3，因此最终结果为9。


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()   
print(f1(), f2(), f3())  # 解决了
