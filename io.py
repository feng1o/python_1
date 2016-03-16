# _*_ coding:utf-8 _*_

f = open('file1.txt', 'r')
print(f.read())
f.close()

# 使用异常
"""try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    print('error,,open,close')
    if f:
    	f.close()"""

# 每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('file1.txt', 'r') as f:
    print(f.read())
# read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，
# 可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以
# 每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。

with open('file1.txt', 'r') as file:
	for line in file.readlines():
		print(line)  

	for line in file.readlines():
		print('strip =%s' % line.strip())  # 吧\n去掉

with open('file1.txt', 'rb') as f:
	print(f.read())

with open('file1.txt', 'r', encoding='utf-8') as f:
	print(f.read())

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
# 因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个
# errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

f = open('file1.txt', 'r', encoding='gbk', errors='ignore')


# xie文件，，
with open('file1.txt', 'w') as fw: 
	#fw.write("write file............................")
with open('file1.txt', 'r') as fw: 
	print(fw.read())