#!/usr/bin/env python

import os
import re


with os.popen('tasklist', 'r') as f:
    for eachLine in f:
    	print(eachLine)
    	print(re.split('\s\s+|\t', eachLine.rstrip()))
