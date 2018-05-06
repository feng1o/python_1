#!/usr/bin/python
# FileName: core1-6.py

import re

bt = 'bat|bet|bit'
pattern = re.compile(bt)
m = re.match(pattern, "bat")
if m is not None:
    print("10....匹配字符串...{}\n".format(m.group()))


# group（n）子组的概念；()来匹配和保存子组

pattern2 = re.compile(r'(\w\w\w)-(\d\d\d)')
m2 = pattern2.match("abc-123")
if m2:
    print(m2.group)
    print(m2.groups())
    print("m2.group(1)= {}".format(m2.group(1)))
    print("m2.group(2)= {0}".format(m2.group(2)))
    print(end='\t\n')


# findall
print(end='\n')
m3 = re.findall("th\w*", "the and That", re.I)
if m3:
    print(m3)
    print(m3[1])


re.purge()
m3 = re.finditer("th\w*", "the and that", re.I)
if m3:
    print(m3)
    print(m3.__next__().group())
    print(m3.__next__().group())


# sub(), subn()替换字符
print("\nsub-------------------")
match = re.sub('[ab]', 'T', 'abcdefagcdef')
print(match)

match = re.subn('[ab]', 'T', 'abcdefabcdef')
print(match)

# 替换分组
print(r"让91年2月20日、20/2/91成为2/20/91； 使用匹配分组（）,然后\N提取分组")
match = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')
print(match)

# ？：扩展部分  与用数字指定组不同的是，它可以用名字来指定。
print("\n\n")
m = re.match("([abc])+", "abc")
print(m.groups())

m = re.match("(?:[abc])+", "abc")
print(m.groups())

p = re.compile(r'(?P<word>\b\w+\b)')
m = p.findall(' Lots of punctuation ')
print(m)
m = p.search(' Lots of punctuation ')
print(m.group('word'))

InternalDate = re.compile(r'INTERNALDATE "'
                          r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
                          r'(?P<year>[0-9][0-9][0-9][0-9])'
                          r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
                          r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
                          r'"')
