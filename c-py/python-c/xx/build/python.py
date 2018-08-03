#!/usr/bin/env python
# coding=utf-8

import ctypes
ll = ctypes.cdll.LoadLibrary
lib = ll("./server.so")
lib.fm(3, "12, 10028, 2")
