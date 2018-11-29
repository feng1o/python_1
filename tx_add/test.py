
# encoding: UTF-8
import re
import datetime
import time

import log_t

INTERVAL = {
                "count-1h": 'hours=-1',
                "count-6h": 'hours=-6',
                "count-1d": 'days=-1',
                "count-6d": 'days=-6'
}

INTERVAL2 = {
                "count-1h": [-1, '-'],
                "count-6h": [-6, ''],
                "count-1d": [-24, ''],
                "count-6d": [-24*30, '']
}
GNUM = 0
def test():
	for i in INTERVAL:
		print (i)
		print (INTERVAL[i])
		print (GNUM)

def test2():
    for  item in INTERVAL2:
        print ("item =", item, INTERVAL2[item][0])
        dt = (datetime.datetime.now()+datetime.timedelta(hours=INTERVAL2[item][0])).strftime("%Y-%m-%d %H:%M:%S")
        #dt = (datetime.datetime.now()+datetime.timedelta(hours=0)).strftime("%Y-%m-%d %H:%M:%S")
        print (dt)
        #转换成时间数组
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
        #转换成时间戳
        timestamp = round(time.mktime(timeArray)*pow(10,9))
        print(timestamp)
        INTERVAL2[item][1] =  timestamp
        print(INTERVAL2[item])
        print(item)

log_t.logging.info("---")