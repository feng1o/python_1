#!/usr/bin/python
# FileName: solve.py

import sys
import warnings
import os
import re

import getName

class CSolve(object):
    """docstring for CSolve.

    CSolve is the class to solve puzzles."""

    cNum = 0
    f = 0
    content = ''

    def __init__(self, FileName, sir, mod):
        super(CSolve, self).__init__()
        self.cNum += 1
        # CSolve.cNum += 1
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
                # self.content = self.content + str(line)
        # CSolve.content.replace('\r', ' ')

    def getSirName(self, sir):
        getName.getName(CSolve.content, self.sir)
