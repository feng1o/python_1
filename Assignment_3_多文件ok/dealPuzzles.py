#!/usr/bin/python
# FileName: dealPuzzles.py

import re
import updateSirId
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
            updateSirId.updateSirIdentity(
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
