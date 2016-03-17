# _*_ coding:utf-8 _*_

from io import StringIO

'''
很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str
'''
f = StringIO()
f.write("hello")
f.write(" ")
f.write("world!")

print(f.getvalue())


f = StringIO("hello \n, world \n !\n")
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


'''BytesIO

StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
'''
from io import BytesIO

b = BytesIO()
b.write('中国'.encode('utf-8'))
print(b.getvalue())
