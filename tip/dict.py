#!/usr/bin/python
# FileName: global_var.py

import sys
import warnings

# sirIdentity = {'a':{flag:-1, 'a':0, b':1, 'c':0}}
# sirIdentity = {'a':[0, {'a':0, b':1, 'c':0}]}

# sirIdentity = {}


def initSirStatus(sirIdentity, names):
    for name1 in names:
        sirIdentity[name1] = {}
        sirIdentity.setdefault(name1, {})['flag'] = -1
        # theIndex.setdefault(word, [ ]).append(pagenumber)  # this is a list
        # sirIdentity[name1].append({'flag':-1})
        for name2 in names:
            sirIdentity.setdefault(name1, {})[name2] = -1
    # print_SirIdentity(sirIdentity, names)


def print_SirIdentity(sirIdentity, names):
    print("%8s" % 'flag', end=' ')
    fnames = names[:]
    # fnames = names.insert(1, 'flag')  # insert no return
    fnames.insert(0, 'flag')
    for name in names:
        print("%5s" % name, end=' ')
    print()
    for key1 in names:
        for key2 in fnames:
            # print("sirIdentity[{0}][{1}] = {2}".format(key1, key2, sirIdentity[key1][key2]), end = ' ')
            print("%5d" % sirIdentity[key1][key2], end=' ')

        print()

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        warnings.warn("python version error...")
    sirIdentity = {}
    names = ['a','b', 'c']
    initSirStatus(sirIdentity,names)
    print_SirIdentity(sirIdentity, names)
