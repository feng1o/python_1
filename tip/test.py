#!/usr/bin/python
#_*_encoding:utf-8_*_
# fileName: getResult.py

import sys
import warnings


def test():
    print("3**2 = {}".format(3**2))
    # num = input("input a num")


def guess(num):
    epsilon = 0.01
    step = epsilon ** 2
    sum = 0.0
    numGess = 0
    while abs(sum**2 - num) >= epsilon and sum <= num:
        sum += step
        numGess += 1
    print("numGess =", numGess, sum)
    print("numGess =", numGess, sum, [1, 2, 3])


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        warnings.warn("error...python3 please", RuntimeError)
    else:
        pass
    test()
    guess(400)
    print("   blank ")
    print("full")