#!/usr/bin/python
# FileName: solve.py

import sys
import warnings
import os
import re

import getName
import dealPuzzles
import CSolve
import getResult

sir = []
sirIdentity = {}

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

    sol = CSolve.CSolve(FileName, sir, 'r+')
    sol.openFile('r')
    sol.readFile()

    # get sir Name
    sol.getSirName(sir)
    dealPuzzles.initSirStatus(sirIdentity, sir)
    
    # print(CSolve.CSolve.content.replace('\n', ' '))

    getName.printSirNames(sir)
    dealPuzzles.getIdentity(sirIdentity, sir, CSolve.CSolve.content)

    # dealPuzzles.print_SirIdentity(sirIdentity, sir)

    rtup = getResult.deal(sirIdentity, sir)
    nResult = rtup[0]
    lastStatus = rtup[1]
    # for key in lastStatus:
        # print(".......................%s" % key)
    if nResult == 0:
        print("There is no solution.")
    elif nResult > 1:
        print("Three are %d solutions." % nResult)
    else:
        print("There is a unique solution:")
        for name in sir:
            if lastStatus[name] == 1:
                print("Sir %s is a Knight." % name)
            else:
                print("Sir %s is a Knave." % name)
    # print(CSolve.content.replace('\n', ' '))
    # del sol
