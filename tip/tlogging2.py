# -*- coding: utf-8 -*-
 
import logging
import sys
import os
 
# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("AppName")
 
# 指定logger输出格式
"""
fmt中允许使用的变量可以参考下表。

    %(name)s Logger的名字
    %(levelno)s 数字形式的日志级别
    %(levelname)s 文本形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s 调用日志输出函数的模块名|
    %(funcName)s 调用日志输出函数的函数名|
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮点数表示|
    %(relativeCreated)d 输出日志信息时的，自Logger创建以来的毫秒数|
    %(asctime)s 字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    %(message)s 用户输出的消息
"""
formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)-8s: %(message)s')
 
# 文件日志
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
 
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值
 
# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
 
# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)
 
# 输出不同级别的log
logger.debug('this is debug info')
logger.info('this is information')
logger.warn('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')
 
# 2016-10-08 21:59:19,493 INFO    : this is information
# 2016-10-08 21:59:19,493 WARNING : this is warning message
# 2016-10-08 21:59:19,493 ERROR   : this is error message
# 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
# 2016-10-08 21:59:19,493 CRITICAL: this is critical message
 
# 移除一些日志处理器
logger.removeHandler(file_handler)
os.system("del test.log")