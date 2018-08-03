# _*_ coding:utf-8 _*_

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute(
    'create table user2(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
cursor.rowcount
cursor.execute('select * from user2 where id=?', ('1',))
cursor.close()

conn.commit()

conn.close()
