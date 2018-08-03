
# encoding: UTF-8
import re
import datetime
import time

def trsTimeStamp(timestamp):
 if len(str(timestamp)) > 11: 
     #print( len(str(timestamp)) )
     timestamp = (int)(timestamp/1000)
 #转换成localtime
 time_local = time.localtime(timestamp)
 #转换成新的时间格式(2016-05-05 20:28:54)
 dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
 #print (dt)
 return dt
#test
timestamp = 1512568774000
#print (trsTimeStamp(timestamp))

#1.转换时间戳
def trsTimeStampSecond(timestamp):
 while len(str(timestamp)) > 11: 
     timestamp = (int)(timestamp/1000)
 #print (timestamp)
 return timestamp



dt = (datetime.datetime.now()+datetime.timedelta(hours=0)).strftime("%Y-%m-%d %H:%M:%S")
print(dt) #2018-03-02 12:57:51
#转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = round(time.mktime(timeArray)*pow(10,9))
print(timestamp)

timestamp = time.mktime(timeArray)
print(timestamp)

print(time.time())  
print(round(time.time()*pow(10,9)))
1519961583.5953999
1519960626169255388
1519961698286400000
1519961745987399936

print (datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))
str1 = " 4.2mb 19248 628.8kb   166 800.6kb  1267 737.2kb   132   1.6mb  7932 "
print(str1)
print("________________")
print(str1.split(' '))


m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print("\n", m.group())

m = re.split('(\d+)' , 'dkjj23jjjj44as')
print(m)

str1 =str1.strip()
lst = re.split('\s+', str1)
print(lst)