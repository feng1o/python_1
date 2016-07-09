#_*_ encoding:utf-8 _*_
# file:

import time

print(time.ctime())


def ispass(base):
    def cmp(val):
        if val >= base:
            print("pass....")
        else:
            print("no pass...")
    return cmp

pass100 = ispass(60)
pass160 = ispass(90)

pass100(88)
pass160(88)
