#!/usr/bin/env python
# coding=utf-8
import ctypes

ll = ctypes.cdll.LoadLibrary
lib = ll("./server.so")
lib.server_c("abcd", 22);
print("....ok...by pyhton");


