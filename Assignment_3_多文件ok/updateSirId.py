#!/usr/bin/python
# FileName: updateSirId.py

import dealPuzzles
import getName

import sys
import re

'''tip:
    all of us are     : 0
    I am a            : 1
    sir \w+       is a: 2
    at least one    of: 3
    at most  one    of: 4
    exactly  one    of: 5
    sir a, b or d is a: 6
    sir a, b and c are: 7'''


def updateIndetity_0(talker, str, sirIdentity, names):
    str = str.replace("Knights", '1')
    str = str.replace("Knaves", '0')
    str = str.replace("Knight", '1')
    str = str.replace("Knave", '0')
    if str.find('1') != -1:
        for name in names:
            sirIdentity[talker][name] = 1
    else:
        for name in names:
            sirIdentity[talker][name] = 0


def updateIndetity_1(talker, str, sirIdentity, names):
    str = str.replace("Knights", '1')
    str = str.replace("Knaves", '0')
    str = str.replace("Knight", '1')
    str = str.replace("Knave", '0')
    if str.find('1') != -1:
        for name in names:
            sirIdentity[talker][talker] = 1
    else:
        for name in names:
            sirIdentity[talker][talker] = 0


def updateIndetity_2(talker, str, sirIdentity, names):
    str = str.replace("Knights", '1')
    str = str.replace("Knaves", '0')
    str = str.replace("Knight", '1')
    str = str.replace("Knave", '0')
    pos = str.find("Sir ")
    str = str[pos + 4:]
    person = ''
    pattern = re.compile(r'\w+')
    match = pattern.match(str)
    if match:
        person = match.group()
    else:
        print("updateIdentity_2 get name error...")
    if str.find('1') != -1:
        for name in names:
            sirIdentity[talker][person] = 1
    else:
        for name in names:
            sirIdentity[talker][person] = 0


def updateIndetity_3(talker, str, sirIdentity, names):
    str = str.replace("Knights", '1')
    str = str.replace("Knaves", '0')
    str = str.replace("Knight", '1')
    str = str.replace("Knave", '0')
    if str.find('us') != -1:
        if str.find('1') != -1:
            for name in names:
                sirIdentity[talker][name] = 1
        else:
            for name in names:
                sirIdentity[talker][name] = 0
    else:
        subNames = []
        getName.getName_up(str, subNames)
        # for name in subNames:
        # print("subname = %s" % name)
        if str.find('1') != -1:
            for name in subNames:
                sirIdentity[talker][name] = 1
        else:
            for name in subNames:
                sirIdentity[talker][name] = 0


def updateIndetity_4(talker, str, sirIdentity, names):
    str = str.replace("Knights", '1')
    str = str.replace("Knaves", '0')
    str = str.replace("Knight", '1')
    str = str.replace("Knave", '0')
    if str.find('us') != -1:
        if str.find('1') != -1:
            for name in names:
                sirIdentity[talker][name] = 1
        else:
            for name in names:
                sirIdentity[talker][name] = 0
    else:
        subNames = []
        getName.getName_up(str, subNames)
        # for name in subNames:
        # print("subname = %s" % name)
        if str.find('1') != -1:
            for name in subNames:
                sirIdentity[talker][name] = 1
        else:
            for name in subNames:
                sirIdentity[talker][name] = 0


def updateIndetity_5(talker, str, sirIdentity, names):
    str = str.replace("Knights", '1')
    str = str.replace("Knaves", '0')
    str = str.replace("Knight", '1')
    str = str.replace("Knave", '0')
    if str.find('us') != -1:
        if str.find('1') != -1:
            for name in names:
                sirIdentity[talker][name] = 1
        else:
            for name in names:
                sirIdentity[talker][name] = 0
    else:
        subNames = []
        getName.getName_up(str, subNames)
        # for name in subNames:
        # print("subname = %s" % name)
        if str.find('1') != -1:
            for name in subNames:
                sirIdentity[talker][name] = 1
        else:
            for name in subNames:
                sirIdentity[talker][name] = 0


def updateIndetity_6(talker, str, sirIdentity, names):
    str = str.replace("Knights", '1')
    str = str.replace("Knaves", '0')
    str = str.replace("Knight", '1')
    str = str.replace("Knave", '0')
    if str.find('us') != -1:
        if str.find('1') != -1:
            for name in names:
                sirIdentity[talker][name] = 1
        else:
            for name in names:
                sirIdentity[talker][name] = 0
    else:
        subNames = []
        getName.getName_up(str, subNames)
        # for name in subNames:
            # print("subname = %s" % name)
        if str.find('1') != -1:
            for name in subNames:
                sirIdentity[talker][name] = 1
        else:
            for name in subNames:
                sirIdentity[talker][name] = 0


def updateSirIdentity(index, talker, str, sirIdentity, names):
    sirIdentity[talker]['flag'] = index
    if index == 0:
        updateIndetity_0(talker, str, sirIdentity, names)
    elif index == 1:
        updateIndetity_1(talker, str, sirIdentity, names)
        # dealPuzzles.print_SirIdentity(sirIdentity, names)
    elif index == 2:
        updateIndetity_2(talker, str, sirIdentity, names)
        # dealPuzzles.print_SirIdentity(sirIdentity, names)
    elif index == 3:
        updateIndetity_3(talker, str, sirIdentity, names)
        # dealPuzzles.print_SirIdentity(sirIdentity, names)
    elif index == 4:
        updateIndetity_4(talker, str, sirIdentity, names)
        # dealPuzzles.print_SirIdentity(sirIdentity, names)
    elif index == 5:
        updateIndetity_5(talker, str, sirIdentity, names)
        # dealPuzzles.print_SirIdentity(sirIdentity, names)
    elif index == 6:
        updateIndetity_6(talker, str, sirIdentity, names)
        # dealPuzzles.print_SirIdentity(sirIdentity, names)
    elif index == 7:
        updateIndetity_6(talker, str, sirIdentity, names)
        # dealPuzzles.print_SirIdentity(sirIdentity, names)