#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
#from sys import maxint
from sys import maxsize
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

print(' '.join(choice(lc) for i in range(23)))
print("".join(choice("liufeng")))
print(end='\n\n')
for i in range(randrange(5, 11)):
	dtint = randrange(maxsize)	# pick date
	dtstr = ctime(dtint)	# date string
	llen = randrange(4, 7)	# login is shorter
	login = ''.join(choice(lc) for j in range(llen))
	dlen = randrange(llen, 13)	# domain is longer
	dom = ''.join(choice(lc) for j in range(dlen))
	print ('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
	dom, choice(tlds), dtint, llen, dlen))
