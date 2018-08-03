# encoding: UTF-8
import re
 
# 将正则表达式编译成Pattern对象
pattern1 = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern1.match('hello world!')
if match:
    # 使用Match获得分组信息
    print(match.group())

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print(m.group())

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
print("\n\n")
pattern = re.compile(r'(Sir|Sirs)\s+\w+')
res = pattern.search('a Sir lf,,, Sirs xx')
if res:print(res.group())
else:
	print("match none")

print(end='\n\n')
str = """a"lf" """
print(str.find("\""))
  

str = 'abcdefghijk'
str1 = str[3:]
print("str = [3:]: " + str1)

print(str1.find("o"))


print("\n\n\n")
patternx = re.compile(r'\s*Sir\s+\w+(,\s\w+)*\s(and){1}\s+\w+\s(are)')
res = patternx.search("Sir Nancy and Andrew are Knaves!")
if res:
	print(res.group())
else:
	print("nothing ")