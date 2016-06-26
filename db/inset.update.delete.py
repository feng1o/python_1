#!/usr/bin/env python3
#_*_ coding:utf-8_*_

import pymysql

conn = pymysql.connect(
    host='192.168.1.120',
    port=3306,
    user='root',
    passwd='feng123',
    charset='UTF8'
)

cur = conn.cursor()

# 选定数据库
cur.execute("use db1")
print(cur.execute("select version()"))

# c查询下数据表里面的lie
cur.execute("SHOW COLUMNS FROM users")
colu = cur.fetchall()
print(" %s \n %s " % colu)

# sql语句
sql_insert = "INSERT INTO users VALUES(100, 'feng')"
sql_update = "UPDATE users SET  name='udpate' where id=3"
sql_delete = "DELETE FROM users  where id>3"

try:  #  比如下面某一不存在，不能操作，其他的就不会被修改
    for i in (1, 2, 3, 4):
        cur.execute(sql_insert)
        print("%d影响了%d 行" % (i, cur.rowcount))
    cur.execute(sql_update)
    print("影响了 %d 行" % cur.rowcount)
    cur.execute(sql_delete)
    print("影响了 %d 行" % cur.rowcount)

    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()  # conn.commit()  # 整除终止 rollback会馆

cur.close()
conn.close()
