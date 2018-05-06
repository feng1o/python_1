# -*- coding: utf-8 -*-
import json
from elasticsearch import Elasticsearch
from influxdb import InfluxDBClient

import time_change



clusterInfo = [("ip1", 9200,"上海测试"), ('ip2', 9200,'张思'), ('ip3', 9200, '王五')]

print(clusterInfo[1][1])
print(len(clusterInfo[0]))
for lst in clusterInfo :
	print(lst)
	for  x in lst:
		print(" %s" % x, end=' ')
	print()


client = InfluxDBClient('localhost', 8086, '', '', '') # 初始化

print ("\n所有数据库:", client.get_list_database())
#client.create_database('testdb') 
#print ("\n所有数据库:", client.get_list_database())
#client.drop_database('testdb') # 删除数据库 
#print ("\n所有数据库:", client.get_list_database())

client = InfluxDBClient('localhost', 8086, 'root', '', 'audit') # 初始化（指定要操作的数据库）
result = client.query('show measurements;') # 显示数据库中的表
print("Result: {0}".format(result))

json_body = [
    {
        "measurement": "students",
        "tags": {
            "stuid": "s123"
        },
        #"time": "2017-03-12T22:00:00Z",
        #"time": str("14895624444444444444"),
        #"time" :"2016-05-05 20:28:54",
        "time" : time_change.trsTimeStamp(1512568774000),
        "fields": {
            "score": 89
        }
    }
]

def showDBNames(client):
        result = client.query('show measurements;') # 显示数据库中的表
        print("Result: {0}".format(result))

client = InfluxDBClient('localhost', 8086, 'root', '', 'audit') # 初始化（指定要操作的数据库）
showDBNames(client)
client.write_points(json_body) # 写入数据，同时创建表
showDBNames(client)
#client.query("drop measurement students") # 删除表
#showDBNames(client)