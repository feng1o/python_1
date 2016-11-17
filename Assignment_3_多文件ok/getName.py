#!/usr/bin/python
# fileName: strGetName.py

import re


def getName(str, names):
    substr = str[:]
    while True:
        pos = substr.find("Sir ")
        if pos == -1:
            break
        # print(pos)
        substr = substr[pos + 4:]
        # print("substr = " + substr)
        pname = re.compile(r'\w+')
        match = pname.match(substr)
        if match:
            name = match.group()
            # print(name)
            if name not in names:
                names.append(name)

    substr = str[:]
    while True:
        pos = substr.find("Sirs ")
        if pos == -1:
            break
        # print(pos)
        substr = substr[pos + 5:]
        # print("substr = " + substr)
        # get names such as A, B,....and/or X./!
        pname = re.compile(r'\w+(,\s\w+)*\s(and|or){1}\s\w+')
        match = pname.match(substr)
        if match:
            mres = match.group()
            # print(mres)
            mres = mres.replace(',', '')
            mres = mres.replace(' and', '')
            mres = mres.replace(' or', '')
            # print(mres)
            tmpNames = mres.split(" ")
            for name in tmpNames:
                if name not in names:
                    names.append(name)
                    # print(name)
def getName_up(str, names):
    substr = str[:]
    while True:
        pos = substr.find("Sir ")
        if pos == -1:
            break
        # print(pos)
        substr = substr[pos + 4:]
        # print("substr = " + substr)
        pname = re.compile(r'\w+(,\s\w+)*\s(and|or){1}\s\w+')
        match = pname.match(substr)
        if match:
            mres = match.group()
            # print(mres)
            mres = mres.replace(',', '')
            mres = mres.replace(' and', '')
            mres = mres.replace(' or', '')
            # print(mres)
            tmpNames = mres.split(" ")
            for name in tmpNames:
                if name not in names:
                    names.append(name)
                    # print(name)

    substr = str[:]
    while True:
        pos = substr.find("Sirs ")
        if pos == -1:
            break
        # print(pos)
        substr = substr[pos + 5:]
        # print("substr = " + substr)
        # get names such as A, B,....and/or X./!
        pname = re.compile(r'\w+(,\s\w+)*\s(and|or){1}\s\w+')
        match = pname.match(substr)
        if match:
            mres = match.group()
            # print(mres)
            mres = mres.replace(',', '')
            mres = mres.replace(' and', '')
            mres = mres.replace(' or', '')
            # print(mres)
            tmpNames = mres.split(" ")
            for name in tmpNames:
                if name not in names:
                    names.append(name)
                    # print(name)

def printSirNames(names):
    names.sort()
    print("The Sirs are:", end=' ')
    for name in names:
        print(name, end=' ')
    print("")

''' used for: test this funciton.
names = []
getName('Yesterday, I visited Sirs Andrew, Lf and Nancy. I asked Sir Andrew who he was, and he answered impatiently: "Sir Nancy and I are Knaves!" Then I met Sir Bill who introduced me to his wife and told me: "at least one of Sir Hilary and I is a Knave." Should I trust them?  Sirs Zhang, Li, Wang or Liu ', names)

'''
