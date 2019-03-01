#!/usr/bin/python
# encoding:utf-8
import os
import mysql.connector
import subprocess
import commands
import sys
import datetime
import time
import random
import logging
from threading import Thread, Event, Lock
import Queue

CLUSTER_ID = 0
DB_HOST = ""
DB_PORT = 0
WEB_HOST = ""

#集群强隔离发布时间，
ISO_TM = '2018-11-27'
hosts=[]

def parse_conf_line(line):
    str = line.rstrip().split('=')[1]
    str = str.split('?')[0]
    str = str.replace("\"", '').strip()
    return str

def get_oss_metadata():
    global CLUSTER_ID,DB_HOST,DB_PORT,HADOOP_CLUSTER_NAME,WEB_HOST
    with open('/usr/local/cdb_mtnc/install/base.conf', 'r') as f:
        for line in f:
            if 'set:default_clusterid=' in line:
                CLUSTER_ID = parse_conf_line(line)
            elif 'set:db_host=' in line:
                DB_HOST = parse_conf_line(line)
            elif 'set:db_port=' in line:
                DB_PORT = parse_conf_line(line)
            elif 'set:cdb_web_ip=' in line:
                WEB_HOST = parse_conf_line(line)
            else:
                pass

    with open('/usr/local/cdb_mtnc/strategy/etc/strategy.conf', 'r') as f:
        for line in f:
            if 'cluster_name' in line:
                HADOOP_CLUSTER_NAME = parse_conf_line(line)
                break

def get_db_connection():
    try:
        conn = mysql.connector.connect(host=DB_HOST, user='root', port=DB_PORT, password='', db='cdb2')
    except Exception, e:
        print e
        sys.exit()
    return conn

def get_all_hosts(conn):
    cursor = conn.cursor()
    #one_week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    sql = "SELECT a.slave_ip,b.slave_port,a.master_ip,b.master_port, b.mem from tb_device_pair a JOIN tb_mysql_pair b ON  a.pair_id=b.device_pair_id JOIN tb_dev_install_type d ON  d.package_id=b.package_id WHERE b.status not in (11) and a.xtype IN ('common','exclusive')   and  b.create_time > '" + ISO_TM + "'"
    logging.info(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    logging.info(res)
    for item in res:
        host = (item[0], item[1], item[4])
        hosts.append(host)
        host = (item[2], item[3], item[4])
        hosts.append(host)
    ro_sql = "select dev.device_ip, ro.port, ro.mem from tb_ro_slave ro  join tb_ro_slave_dev dev on dev.id = ro.ro_slave_dev_id join tb_dev_install_type dtype on dtype.package_id = ro.package_id  where dev.xtype IN ('common','exclusive')  and ro.status not in (11) and ro.update_time > '"  + ISO_TM + "'"
    logging.info(ro_sql)
    cursor.execute(ro_sql)
    roRes = cursor.fetchall()
    for item in roRes:
        host = (item[0], item[1], item[2])
        hosts.append(host)
    cursor.close()

def conn_inst(item):
    logging.info("\n")
    logging.info(" #################---->deal hosts = [%s,%d] ############## " % (item[0],item[1]))
    try:
        conn = mysql.connector.connect(host=item[0], user='tencentroot', port=int(item[1]), password='', db='')
    except mysql.connector.errors.InterfaceError as e:
        logging.error(e)
        return (-1, None)
    return (0, conn)


def start_fix_conf():
    for item in hosts:
        errno, conn = conn_inst(item)
        if errno != 0 :
            continue
        cursor = conn.cursor()
    try:
            res = "show global variables like 'datadir'"
            logging.info(res)
            cursor.execute(res)
    except :
        print("查询datadir失败，需检查实例系统表是否异常,(%s,%d)" %(item[0], item[1]))
        logging.error("查询datadir失败，需检查实例系统表是否异常,(%s,%d)" %(item[0], item[1]))
        continue
        dataDirArr = cursor.fetchone()
        baseDir = dataDirArr[1]
        logging.info("data dir  = {0}".format(baseDir))
        initMaxConn = int(800 if item[2] < 4000 else (item[2]/5, 10240)[item[2] > 51200])
        inLine = "max_connections = " + str(initMaxConn)
        cmd = "ajs_client_cmd  \"cd " + baseDir + " ; cp my.cnf my.cnf.iso_bak; sed '/max_connections/d' -i  my.cnf ; sed '/open_files_limit/a" + inLine + "' -i my.cnf " + "\" " + item[0]
        logging.info(cmd[0:len(cmd)-0])
        ret = subprocess.call(cmd, shell=True)
        if ret != 0:
            logging.error("Failed to add conf  in (%s, %d)" % (item[0], item[1]))
        else:
            logging.info("#################---->Add conf in (%s, %d) success##############" % (item[0],item[1]))

if __name__ == '__main__':
    install_tools = True
    if len(sys.argv) != 2:
        print 'iso deploy time needed'
        sys.exit()
    ISO_TM = sys.argv[1]

    get_oss_metadata()
    conn = get_db_connection()
    logfile_name = 'fix_max_conn.log'
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%F %H:%M:%S',
                filename=logfile_name,
                filemode='w')
    get_all_hosts(conn)
    start_fix_conf()


