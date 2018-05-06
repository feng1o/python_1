#!/usr/bin/env python

from atexit import register
from random import randrange, choice
from string import ascii_lowercase as lc
from threading import Thread, Lock, currentThread
import string
#from sys import maxint
from sys import maxsize
from time import ctime, sleep

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(10):
	print(i)
#
print('- '.join(choice(lc) for i in range(23)))
print("".join(choice("liufeng")))

# random.range
print("randrange {0}".format(randrange(9, 10)))
print("randrange {0}".format(randrange(3)))
print(ctime())
print(lc)
print(string.ascii_uppercase)
print(end='\n\n')


for i in range(randrange(5, 11)):
    dtint = randrange(maxsize)  # pick date
    dtstr = ctime(dtint)  # date string
    llen = randrange(4, 7)  # login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)  # domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
                                      dom, choice(tlds), dtint, llen, dlen))

#print((randrange(2, 5) for x in xrange(randrange(5))))

class CleanOutputSet(set):

    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
print('loops结果是', loops)
remaining = CleanOutputSet()


def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    # print '[{0}] Started {1}'.format(ctime(), myname)
    print('[%s] Started %s' % (ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % (  # print '[{0}] Completed {1} ({2} secs)'.format(
        ctime(), myname, nsec))
    # print '    (remaining: {0})'.format(remaining or 'NONE')
    print('    (remaining: %s)' % (remaining or 'NONE'))
    lock.release()


def _main():
    for pause in loops:
        print("pause == ", pause)
        Thread(target=loop, args=(pause,)).start()
_main()
@register  	# 注册一个退出函数
def _atexit():
    print("\nexit = ", ctime())
