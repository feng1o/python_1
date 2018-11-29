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
HADOOP_CLUSTER_NAME = ""
HADOOP_MAX_JOB_PER_NODE = 2
CDB_MAX_JOB_PER_NODE = 3
NUM_OF_CONSUMERS = 0
MOD_ID = 0
CMD_ID = 0

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
    sql = "SELECT a.slave_ip,b.slave_port,a.master_ip,b.master_port from tb_device_pair a JOIN tb_mysql_pair b ON  a.pair_id=b.device_pair_id JOIN  tb_app_inst  c ON  c.instance_id=b.app_id JOIN tb_dev_install_type d ON  d.package_id=b.package_id WHERE b.status not in (11) and d.mysql_version='5.7' and  c.create_time > '2018-08-10'  limit 2 "
    logging.info(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    logging.info(res)
    for item in res:
        host = (item[0], item[1])
        hosts.append(host)
        host = (item[2], item[3])
        hosts.append(host)
    ro_sql = "select dev.device_ip, ro.port from tb_ro_slave ro  join tb_ro_slave_dev dev on dev.id = ro.ro_slave_dev_id join tb_dev_install_type dtype on dtype.package_id = ro.package_id  where dtype.mysql_version = '5.7' and ro.status not in (11) and ro.update_time > '2018-07-10'"
    logging.info(ro_sql)
    cursor.execute(ro_sql)
    roRes = cursor.fetchall()
    logging.info("ro inst ip port  =  %s" % roRes)
    for item in roRes:
        host = (item[0], item[1])
        hosts.append(host)
    cursor.close()

def conn_inst(item):
    logging.info("\n")
    logging.info("-----------------deal hosts = [%s,%d] -------------- " % (item[0],item[1]))
    try:
        conn = mysql.connector.connect(host=item[0], user='tencentroot', port=int(item[1]), password='', db='')
    except mysql.connector.errors.InterfaceError as e:
        logging.error(e)
        return (-1, None)
    return (0, conn)


def start_audit_plugin():
    #hosts.append(("10.108.93.21",20160))
    #hosts.append(("10.108.93.21",20160))
    for item in hosts:
        errno, conn = conn_inst(item)
        if errno != 0 :
            continue
        cursor = conn.cursor()
        sqlVerCommon = "show global variables like 'version_comment'"
        #logging.info(sqlVerCommon)
        cursor.execute(sqlVerCommon)
        versionCommon = cursor.fetchone()

        sqlVer = "show global variables like 'version'"
        #logging.info(sqlVer)
        res = cursor.execute(sqlVer)
        version = cursor.fetchone()
        logging.info("verson = {}, version_comment = {}".format(version[1], versionCommon[1]))
        #if versionCommon[1] == "20180530" and version[1] == "5.7.18-txsql-log":
        if versionCommon[1] == "20170531" and version[1] == "5.7.18-txsql-log":
            logging.info("----------------->start install plugin")
            logging.info("\t\t ip: %s,port: %s" % (item[0], item[1]))
            sql = "install plugin audit_cdb soname 'audit_cdb.so'"
            logging.info(sql)
            try:
                cursor.execute(sql)
                conn.commit()
            except mysql.connector.errors.DatabaseError as e:
                logging.error("发生错误： %s" %  e)
            finally:
                conn.close()
                cursor.close()

            """
            datadirSql = "show global variables like 'datadir'"
            cursor.execute(datadirSql)
            res = cursor.fetchone()
            datadir = res[1]
            logging.info("data dir = %s " % datadir)
            mycnf = datadir + "my.cnf"
            bak_mycnf = datadir + "my.cnf.bak57"
            cmd = "ajs_client_cmd -t 600 'cp '" + mycnf + " " + bak_mycnf + " " + item[0]
            logging.info(cmd)
            ret = subprocess.call(cmd, shell=True)
            if ret != 0:
                logging.warning("Failed to backup cnf  %s" % item[0])
            else:
                logging.info("backup conf in %s success" % item[0])
            cmdEnablePlugin = "ajs_client_cmd \"sed '/tencent_myisam_conversion_innodb/a\#audit plugin\nplugin-load-add=audit_cdb=audit_cdb.so\n#audit_cdb=FORCE_PLUS_PERMANENT' -i " + mycnf + " "  + item[0]
            logging.info(cmdEnablePlugin)
            ret = subprocess.call(cmdEnablePlugin, shell=True)
            if ret != 0:
                logging.warning("Failed to add conf  in %s" % item[0])
            else:
                logging.info("add conf  in %s success" % item[0])
            """


if __name__ == '__main__':
    install_tools = True
    if len(sys.argv) != 1:
        try:
            flag = int(sys.argv[1])
        except ValueError:
            print 'the install_tools flag must be integer'
            sys.exit()

        if flag == 0:
            install_tools = False

    get_oss_metadata()
    conn = get_db_connection()
    logfile_name = 'BACKUP_MIGRATION.log'
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%F %H:%M:%S',
                #filename=logfile_name,
                filemode='w')
    get_all_hosts(conn)
    start_audit_plugin()
