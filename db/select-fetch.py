#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
print(cur)
for i in cur:
    print(i)
cur.execute('use db1')


sql = 'select * from users'
cur.execute(sql)
print(cur.rowcount)

rs = cur.fetchone()
print(rs)

rs = cur.fetchmany(3)
print(rs)

rs = cur.fetchall()
print(rs)

for row in rs:
	print("userid = %d , username=%s" % row) #row是一个元组

cur.close()
conn.close()
