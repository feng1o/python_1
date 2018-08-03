#_*_ coding: utf-8 _*_

numa = ord('a')
print(numa)
print('sba')
print("编码。。。。。。。。。。。")
print(chr(12))
print('\u4e2d\u6587')
print("编码。.encode('utf-8')。。。。。。。。。。")
print('ab'.encode('utf-8'))
print("编码。。decode(_。。。。。。。。。")
print(b'ABC'.decode('ascii'))  # b就是一个字节，，，，，

print('len = %d' % len("abc"))  # %和c里面一样，，，，

"""
>>> dict = {"asdf": "我们的python学习"}
>>> print dict
{'asdf': '\xe6\x88\x91\xe4\xbb\xac\xe7\x9a\x84python\xe5\xad\xa6\xe4\xb9\xa0'}
在输出处理好的数据结构的时候很不方便，需要使用以下方法进行输出：
>>> import json
>>> print json.dumps(dict, encoding="UTF-8", ensure_ascii=False)
{"asdf": "我们的python学习"}
注意上面的两个参数

如果是字符串，直接输出或者
print str.encode("UTF-8")
"""