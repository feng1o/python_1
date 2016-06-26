#!/usr/bin/bash
#_*_conding:utf-8_*_

import pymysql

conn = pymysql.connect(
    host='192.168.1.120',
    port=3306,
    user='root',
    passwd='feng123',
    charset='UTF8'
)
cur = conn.cursor()

cur.execute("select version()")
print("数据库版本为：")
ver = cur.fetchall()
print(ver)

#  选择数据库
try:
    cur.execute("use db1")
    cur.execute("SHOW COLUMNS FROM users")
    col = cur.fetchall()
    print("列结构%s %s\n" % col)
except Exception as e:
    print("erorr: %s" % e)
else:
    print("else")
finally:
    print("rollback")
    conn.rollback()

try:
	sql = "SELECT distinct id FROM users"
	cur.execute(sql)
	print("不同的列id%s %s %s "% cur.fetchall())	
	cur.execute("select users.id from users limit 2,16")
	print("同的列id ", cur.fetchall())	
except Exception as e:
	raise
else:
	pass
finally:
	pass

cur.close()
conn.close()
