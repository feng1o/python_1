#!/usr/bin/python
# FileName: dealPuzzles.py

'''tip:
    at least one    of: 1
    at most  one    of: 2
    exactly  one    of: 3
    sir x1,x2 or x3 is: 3
    other             : 4
    no say            : 5'''

names = ['a', 'b', 'c']
# sirIdentity = {'a':{flag:-1, 'a':0, b':1, 'c':0}}
# sirIdentity = {'a':[0, {'a':0, b':1, 'c':0}]}

sirIdentity = {}

def initSirStatus(sirIdentity, names):
    for name1 in names:
        sirIdentity[name1] = {}
        sirIdentity.setdefault(name1, {})['flag'] = -1
        # theIndex.setdefault(word, [ ]).append(pagenumber)  # this is a list
        # sirIdentity[name1].append({'flag':-1})
        for name2 in names:
            sirIdentity.setdefault(name1, {})[name2] = -1

# print(sirIdentity['a']['c'])

initSirStatus(sirIdentity, names)
fnames = names[:]
# fnames = names.insert(1, 'flag')  # insert no return
fnames.insert(0, 'flag')
for key1 in names:
    for key2 in fnames:
        print("sirIdentity[{0}][{1}] = {2}".format(key1, key2, sirIdentity[key1][key2]))
