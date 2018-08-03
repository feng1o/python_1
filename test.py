#_*_ encoding:utf-8 _*_

# import mysql.connector
import pymysql
# change root password to yours:
#　conn = mysql.connector.connect(user = 'root', password = 'feng123', database = 'test')
conn=pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'feng123', db = 'mysql', charset = 'UTF8')

cursor=conn.cursor()
# 创建user表:
cursor.execute(
    'create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print 'rowcount =', cursor.rowcount
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor=conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values=cursor.fetchall()
print values
# 关闭Cursor和Connection:
cursor.close()
conn.close()