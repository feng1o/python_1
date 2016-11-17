#!/usr/bin/python
# fileName: getResult.py

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
