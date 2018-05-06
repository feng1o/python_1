#coding:UTF-8
import time
import datetime
 
#1.转换时间戳
def trsTimeStamp(timestamp):
	if len(str(timestamp)) > 11: 
		timestamp = timestamp/1000
	#转换成localtime
	time_local = time.localtime(timestamp)
	#转换成新的时间格式(2016-05-05 20:28:54)
	dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	#print (dt)
	return dt
#test
timestamp = 1512568774000
print (trsTimeStamp(timestamp))
timestamp = 1512568774000/1000


# #转换成localtime
# time_local = time.localtime(timestamp)
# #转换成新的时间格式(2016-05-05 20:28:54)
# dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
# print (dt)


print (datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))