#!/usr/bin/python
# FileName: solve.py

import sys
import warnings
import os
import re

sir = []
sirIdentity = {}

# File: getName.py........................................................
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
    print('The Sirs are: ' + ' '.join(names) + ' ')
    # print('The Sirs are: ' + ' '.join(names))
    '''print("The Sirs are:", end=' ')
    for name in names:
        print(name, end=' ')
    print("")'''


#  Csolve.py..........................................................................
class CSolve(object):
    """docstring for CSolve.

    CSolve is the class to solve puzzles."""

    cNum = 0
    f = 0
    content = ''

    def __init__(self, FileName, sir, mod):
        super(CSolve, self).__init__()
        CSolve.cNum += 1
        self.FileName = FileName
        self.mod = mod
        self.sir = sir
        # CSolve.f = open(self.FileName, self.mod)
        # print("fileName = %s, class num = %d" % (self.FileName, CSolve.cNum))

    def __del__(self):
        CSolve.cNum -= 1
        self.closeFile()
        # print("class initialized nums is : {}".format(CSolve.cNum))

    def openFile(self, mod):
        if CSolve.f == 0:
            CSolve.f = open(self.FileName, self.mod)
            # print("CSolve.f= {0}".format(CSolve.f))

    def closeFile(self):
        if CSolve.f != 0:
            CSolve.f.close()

    def readFile(self):
        while True:
            line = CSolve.f.readline()
            if len(line) == 0:
                break
            else:
                # print(line)
                # print(str(line).find('S'))
                CSolve.content = CSolve.content + str(line)
        # CSolve.content.replace('\r', ' ')

    def getSirName(self, sir):
        getName(CSolve.content, self.sir)


# updateSirId.py....................................................................
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
        getName_up(str, subNames)
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
        getName_up(str, subNames)
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
        getName_up(str, subNames)
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
        getName_up(str, subNames)
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

#  dealPuzzle.py...................................................................
'''tip:
    all of us are     : 0
    I am a            : 1
    sir \w+       is a: 2
    at least one    of: 3
    at most  one    of: 4
    exactly  one    of: 5
    sir a, b or d is a: 6
    sir a, b and c are: 7'''

# sirIdentity = {'a':{flag:-1, 'a':0, b':1, 'c':0}}
# sirIdentity = {'a':[0, {'a':0, b':1, 'c':0}]}

# sirIdentity = {}

reg = [
    r'\s*[Aa]ll of us are\s+',
    r'\s*I am a\s+',
    r'\s*Sir \w+ is a\s+',
    r'\s*[aA]t least one of\s+',
    r'\s*[Aa]t most one of\s+',
    r'\s*[Ee]xactly one of\s+',
    r'\s*Sir\s\w+(,\s\w+)*\s(or){1}\s+\w+\s+(is a)',
    r'\s*Sir\s\w+(,\s\w+)*\s(and){1}\s+\w+\s+(are)']

pattern = []
# print(reg[0])


def reCompile(reg):
    for i in range(8):
        pattern.append(re.compile(reg[i]))


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


def initSirStatus(sirIdentity, names):
    for name1 in names:
        sirIdentity[name1] = {}
        sirIdentity.setdefault(name1, {})['flag'] = -1
        # theIndex.setdefault(word, [ ]).append(pagenumber)  # this is a list
        # sirIdentity[name1].append({'flag':-1})
        for name2 in names:
            sirIdentity.setdefault(name1, {})[name2] = -1
    # print_SirIdentity(sirIdentity, names)


'''
# pattern = re.compile(r'[aA]t least one of\s')
pattern = re.compile(reg[0])
match = pattern.match("At least one of Sir Lf")
if match:
    print(match.group()) '''
# test initsir
# initSirStatus(sirIdentity, names)

# content = 'One evening as you are out for a stroll, you walk by a doorway labeled no normals allowed. Some people are talking inside. Curious, you listen, and you hear Sir Paul who says: "all of us are Knaves." "Exactly one of us is a Knight," replies Sir Jenny. As for Sir John, who is also inside, he just keeps quiet. Who is a Knight, and who is a Knave?'


def getDealStr(content):
    dotPos = content.find('.')
    dQuotPos = content.find('"')
    if dotPos != -1:
        while dotPos < dQuotPos:
            content = content[dotPos + 2:]
            # print(content)
            dotPos = content.find('.')
            if dotPos == -1:
                break
    tanPos = content.find('!')
    dQuotPos = content.find('"')
    # print((tanPos,dQuotPos))
    if tanPos != -1:
        while tanPos < dQuotPos:
            content = content[tanPos + 2:]
            # print(content)
            tanPos = content.find('!')
            if tanPos == -1:
                break
    endDotPos = content.find('.')
    endTanPos = content.find('!')
    end = len(content)
    if (endDotPos >= 0 and endTanPos >= 0 and endDotPos < endTanPos):
        end = endDotPos
    elif(endDotPos >= 0 and endTanPos >= 0 and endDotPos >= endTanPos):
        end = endTanPos
    elif(endDotPos > 0 and endTanPos < 0):
        end = endDotPos
    elif(endDotPos < 0 and endTanPos > 0):
        end = endTanPos
    substr = content[:end + 2]
    leftStr = content[end + 2:]
    return [substr, leftStr]


def getSaySir(str):
    pos = str.find('"')
    lstr = str[:pos]
    sirPos = lstr.find("Sir ")
    if sirPos != -1:
        substr = lstr[sirPos + 4:]
        substr = substr.replace('.', '')
        substr = substr.replace('!', '')  
        # print("\nlsubstr = %s\n" % substr)
        pname = re.compile(r'\s*\w+')
        match = pname.match(substr)
        if match:
            name = match.group()
            return name
    else:
        midStr = str[pos + 1:]
        rstr = midStr[midStr.find('"') + 1:]
        rSirPos = rstr.find("Sir ")
        if rSirPos != -1:
            substr = rstr[rSirPos + 4:]
            substr = substr.replace('.', '')
            substr = substr.replace('!', '')            
            # print("\nrsubstr = %s\n" % substr)
            pname = re.compile(r'\s*\w+')
            match = pname.match(substr)
            if match:
                name = match.group()
                return name


def getWhatToSay(talker, substr, sirIdentity, names):
    # print("................" + substr)
    lquote = substr.find('"')
    substr = substr[lquote + 1:]
    rquote = substr.find('"')
    substr = substr[:rquote]
    # substr = substr.replace('I', talker)
    sirPos = substr.find("Sir")
    if sirPos != -1:  # delte other Sir keywords
        tmpStr = substr[sirPos + 3:]
        tmpStr = tmpStr.replace(' Sir', '')
        substr = substr[:sirPos + 3] + tmpStr
    flag = False
    for i in range(8):
        if(i >= 3 and flag == False):
            substr = substr.replace('I', talker)
            flag = True
        # else:
            # print((i, flag))
        result = pattern[i].search(substr)
        # print("...........match ...substr= %s " % substr)
        # print(i)
        # print(reg[i])
        if result:
            # print("---------------" + substr)
            # print(result.group())
            updateSirIdentity(
                i, talker, substr, sirIdentity, names)
            break


def getIdentity(sirIdentity, names, content):
    reCompile(reg)
    content = content.replace('\n', ' ')
    # print("\ncontent: \n      " + content)
    # get deal string
    while True:
        dealStr = getDealStr(content)
        substr = dealStr[0]
        # print("\n\n\nsubcontent: \n      " + substr)
        # print("\nlefcontent: \n      " + dealStr[1])
        saySir = getSaySir(substr)  # get the Sir who tells the identity
        # print("saySir = {}".format(saySir))

        getWhatToSay(saySir, substr, sirIdentity, names)
        content = dealStr[1]
        if content.find('"') == -1:
            break

#  getResult.py.....................................................................
nSolution = 0
lastStatus = {}


def isOk_00(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        for name in names:
            if sirStatus[name] != 1:
                return False
        return True
    else:
        for name in names:
            if sirStatus[name] == 1:
                return True
        return False


def isOk_0(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num == len(subNames):
            return True
        else:
            return False
    else:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num != len(subNames):
            return True
        else:
            return False


def isOk_1(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        if sirIdentity[saySir][saySir] == 1:
            return True
        else:
            return False
    else:
        if sirIdentity[saySir][saySir] == 1:
            return True
        else:
            return False


def isOk_2(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        for name in names:
            if sirIdentity[saySir][name] != -1:
                if sirIdentity[saySir][name] != sirStatus[name]:
                    return False
        return True
    else:
        for name in names:
            if sirIdentity[saySir][name] != -1:
                if sirIdentity[saySir][name] == sirStatus[name]:
                    return False
        return True


def isOk_3(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num > 0:
            return True
        else:
            return False
    else:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num == 0:
            return True
        else:
            return False


def isOk_4(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num <= 1:
            return True
        else:
            return False
    else:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num > 1:
            return True
        else:
            return False


def isOk_5_2(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        for name in names:
            if sirIdentity[saySir][name] != -1:
                if sirIdentity[saySir][name] != sirStatus[name]:
                    return False
        return True
    else:
        for name in names:
            if sirIdentity[saySir][name] != -1:
                if sirIdentity[saySir][name] == sirStatus[name]:
                    return False
        return True


def isOk_5(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num == 1:
            return True
        else:
            return False
    else:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num != 1:
            return True
        else:
            return False

def isOk_6(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num > 0:
            return True
        else:
            return False
    else:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num != 1:  # knave say : will not one match error
            return True
        else:
            return False


def isOk_7(saySir, sirIdentity, names, sirStatus):
    if sirStatus[saySir] == 1:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num == len(subNames):
            return True
        else:
            return False
    else:
        num = 0
        subNames = []
        friendFlag = -1
        for name in names:
            if sirIdentity[saySir][name] != -1:
                friendFlag = sirIdentity[saySir][name]
                subNames.append(name)
        for name in subNames:
            if sirStatus[name] == friendFlag:
                num += 1
        if num != len(subNames):
            return True
        else:
            return False


switch = {
    0: isOk_0,
    1: isOk_1,
    2: isOk_2,
    3: isOk_3,
    4: isOk_4,
    5: isOk_5,
    6: isOk_6,
    7: isOk_7}


def isRight(sirIdentity, names, sirStatus):
    for name in names:
        flag = sirIdentity[name]['flag']
        if flag != -1:
            # print("switch [%s] " % flag)
            bl = switch[flag](name, sirIdentity, names, sirStatus)
            if bl == False:
                return False
    return True


def perm(sirStatus, names, index, len, sirIdentity):
    if index == len:
        '''for key in sirStatus:
            print(sirStatus[key], end=' ')
        print(" getResult 224.....")'''
        flag = isRight(sirIdentity, names, sirStatus)
        if flag == True:
            global nSolution
            global lastStatus
            # lastStatus = sirStatus
            for key in sirStatus:
                lastStatus[key] = sirStatus[key]
            nSolution += 1
            '''
            print("......................ok.............== %s " % nSolution)
            for key in sirStatus:
                print(sirStatus[key], end=' ')
            print("...ok.....last result.........\n\n")
            '''
        return
    if index < len:
        for i in range(2):
            sirStatus[names[index]] = i
            perm(sirStatus, names, index + 1, len, sirIdentity)


def perm2(sirStatus, names, index, len, sirIdentity):
    if index == len - 1:
        flag = isRight(sirIdentity, names, sirStatus)
        if flag == True:
            lastStatus = sirStatus
            # print("......................ok.............== %s " % nSolution)
            for key in sirStatus:
                print(sirStatus[key], end=' ')
            print()
            return 1
        else:
            return 0
    if index < len - 1:
        for i in range(2):
            sirStatus[names[index]] = i
            return nSolution + perm2(sirStatus, names, index + 1, len, sirIdentity)


def deal(sirIdentity, names):
    sirStatus = {}
    for name in names:
        sirStatus[name] = 0
    length = len(names)
    index = 0
    perm(sirStatus, names, index, length, sirIdentity)
    # print("+++++++++++++++++num = %s" % nSolution)
    return (nSolution, lastStatus)


#  main..............................................................................
if __name__ == '__main__':
    if sys.version_info[0] < 3:
        warnings.warn("Need python 3.0  for this program", RuntimeError)
    else:
        pass
        # print("running....")
    # FileName = sys.argv[0]
    FileName = input("Which text file do you want to use for the puzzle? ")
    # FileName = 'my_test7.txt'
    """f = open(FileName, 'r')
    print(f.readline())"""

    sol = CSolve(FileName, sir, 'r+')
    sol.openFile('r')
    sol.readFile()

    # get sir Name
    sol.getSirName(sir)
    initSirStatus(sirIdentity, sir)

    # print(CSolve.content.replace('\n', ' '))

    printSirNames(sir)
    getIdentity(sirIdentity, sir, CSolve.content)

    # print_SirIdentity(sirIdentity, sir)

    rtup = deal(sirIdentity, sir)
    nResult = rtup[0]
    lastStatus = rtup[1]
    # for key in lastStatus:
    # print(".......................%s" % key)
    if nResult == 0:
        print('There is no solution.')
    elif nResult > 1:
        print("Three are %d solutions." % nResult)
    else:
        print("There is a unique solution:")
        for name in sir:
            if lastStatus[name] == 1:
                print("Sir %s is a Knight." % name)
            else:
                print("Sir %s is a Knave." % name)
    # print(content.replace('\n', ' '))
    # del sol
