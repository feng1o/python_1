#!/usr/bin/python
# Filename: str_methods.py

# help(str)
import string

name = 'Swaroop a,b,c, kkkk' # This is a string object

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

print("strip----" + name.strip().lstrip(',').rstrip(','))
print(name)
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

print("atoi."123".{}".format(atoi('123')))
input()