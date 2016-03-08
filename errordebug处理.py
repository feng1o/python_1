# _*_ coding:utf-8 _*_

# 高级语言通常都内置了一套
#　try...except...finally...的错误处理机制，Python也不例外。
#　当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，
#  则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#  执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

try:
    print("try")
    r = 10 / 0
    print("result = %d" % r)


except ZeroDivisionError as e:
    print('except:', e)

finally:
    print('finally...')
print('END')


try:
    print('try...')
    r = 10 / int('a')  # 跳到后面的except了，
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print("no error!")
finally:
    print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

# 多层调用


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
main()

try:
	print("try")
   # s = 10 / 0
except ValueError as e:
    print('ValueError')
except UnicodeError as e:  # 永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类
    print('UnicodeError')
finally:
	pass


# 调用堆栈
# 错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印错误信息，然后程序退出
# err.py:
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')

main()


#  记录错误  Python内置的logging模块可以非常容易地记录错误信息
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)  # 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：

main()
print('END')


# 跑出错误
# 先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
# err_raise.py
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
