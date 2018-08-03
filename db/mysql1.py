#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########
import pymysql
print(pymysql)


conn = pymysql.connect(
    host='127.0.0.1',
    #host=localhost,
    port=3306, user='root',
    passwd='feng123',
    db='mysql',
  #  charset='UTF8'
    # db='mysql',
    charset='UTF8'
)  # connection
cur = conn.cursor()  # coursion 交互
cur.execute("select version()")
print('\n')
for i in cur:
    print(',,%s' % i)
cur.execute("use digitalchip")
# cur.execute("CREATE TABLE users(id INT, name VARCHAR(20))")
cur.execute("INSERT INTO  userlogin VALUES(1,'lf'), (2, 'x'), (3, 'b')")

cur.execute("select * FROM userlogin")
data = cur.fetchall()

for row in data:
	print('%s \t %s' %row)


cur.close()
conn.commit()
conn.close()

'''
# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

# import mysql.connector
import pymysql
# change root password to yours:
#　conn = mysql.connector.connect(user = 'root', password = 'feng123', database = 'test')
conn=pymysql.connect(host = '192.168.1.120', port = 3306, user = 'root', passwd = 'feng123', db = 'mysql', charset = 'UTF8')

cursor=conn.cursor()
# 创建user表:
cursor.execute(
    'create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor=conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values=cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
'''
