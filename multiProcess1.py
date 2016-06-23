#_*_ coding:utf-8_*_

#file: multiprocess 
#by:lf

print ('multiprocess')

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_fun(name):
	print('sub process :%s ..id:%s' % (name, os.getpid()))
if __name__ == '__main__':
	print ('father process %s...'  %  os.getpid())
	p = Process(target=run_fun, args = ('test',))
	print('child start..')
	p.start()
	p.join()  # wait subprocess to do 
	print('child process end ....')

"""
import os
print('process %s start...' % os.getpid())
pid = os.fork()
if  pid == 0:
	print('in child process %s ' % os.getpid())
else :
	print("father process id %s ..." % os.getppid())
"""

