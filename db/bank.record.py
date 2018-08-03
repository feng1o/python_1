#!/usr/bin/env python3
#_*_ coding:utf-8_*_

import pymysql
import sys

conn = pymysql.connect(
    host='192.168.1.120',
    port=3306,
    user='root',
    passwd='feng123',
    charset='UTF8'
)

cur = conn.cursor()
cur.execute("select version()")
print("mysql version is:")
for i in cur:
    print(i)

cur.execute("USE db1")
try:
    sql_createTable = "CREATE TABLE account(id INT DEFAULT NULL COMMENT 'id', money INT)"
    cur.execute(sql_createTable)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
print("roll back")

cur.execute("SHOW columns from account")
columns = cur.fetchall()
print("表结构\n %s \n %s \n\n" % columns)


class TransferMoney(object):
    """docstring for TransferMoney"""

    def __init__(self, arg):
        super(TransferMoney, self).__init__()
        self.arg = arg

    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = " select * from account where id=%s" % acctid
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号error %s" % acctid)
        finally:
            cursor.close()

    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = " select * from account where id=%s and money>%s" % (
                acctid, money)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号没有足够钱 %s" % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE account set money=money-%s where id=%s" % (
                money, acctid)
            cursor.execute(sql)
            print("add money + %s" % sql)
            if cursor.rowcount != 1:
                raise Exception("账号error %d减款失败" % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE account set money=money+%s where id=%s" % (
                money, acctid)
            cursor.execute(sql)
            print("add money + %s" % sql)
            if cursor.rowcount != 1:
                raise Exception("账号error %djia款失败" % acctid)
        finally:
            cursor.close()

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(target_acctid)
            self.check_acct_available(source_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


if __name__ == "__main__":
	source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    ty_money = TransferMoney()

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print("错误：%s " % e)
    finally:
        conn.close()


cur.close()
conn.close()
