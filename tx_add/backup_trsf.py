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
DB_CHECK_INTERVAL = 600
HADOOP_CLUSTER_NAME = ""
HADOOP_MAX_JOB_PER_NODE = 2
CDB_MAX_JOB_PER_NODE = 3
NUM_OF_CONSUMERS = 0
MOD_ID = 0
CMD_ID = 0
BUCKET_HOST = ""

lock = Lock()
sentinel = object()

def parse_cos_conf_file():
    global MOD_ID, CMD_ID, BUCKET_HOST
    with open('/data/cdb2cos/etc/cdb2cos.conf') as f:
        for line in f:
            if 'cos_bucket_cl5_mod_id=' in line:
                MOD_ID = int(line.rstrip().split('=')[1])
            elif 'cos_bucket_cl5_cmd_id=' in line:
                CMD_ID = int(line.rstrip().split('=')[1])
            elif 'cos_bucket_host=' in line:
                BUCKET_HOST = line.rstrip().split('=')[1]
            else:
                pass
    
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def get_db_connection():
    try:
        conn = mysql.connector.connect(host=DB_HOST, user='root', port=DB_PORT, password='', db='cdb2')
    except Exception, e:
        print e
        sys.exit()

    return conn

def parse_conf_line(line):
    str = line.rstrip().split('=')[1]
    str = str.split('?')[0]
    str = str.replace("\"", '').strip()
    return str

def create_tmp_table(conn):
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS `tmp_cos_upload_task`(`id` int(11) NOT NULL AUTO_INCREMENT, `status` enum('WAITING','RUNNING','FINISHED','FAILED') NOT NULL, "\
            "`start_time` datetime DEFAULT '0000-00-00 00:00:00', `end_time` datetime DEFAULT '0000-00-00 00:00:00', `path` varchar(2048) NOT NULL, `retry_count` tinyint(1) NOT NULL, "\
            "`type` enum('hadoop','hadoop_nolock','mydumper','mydumper_nolock','xtrabackup','xtrabackup_nolock') NOT NULL, `new_size` bigint(20) NOT NULL, `old_size` bigint(20) NOT NULL, "\
            "PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8"
    logging.info(sql)
    cursor.execute(sql)
    cursor.close()

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

def get_hadoop_datanodes():
    nodelist = []
    cmd = "hadoop dfsadmin -report | grep -B1 Normal | grep Name | awk '{print $2}' | awk -F: '{print $1}'"
    retcode, output = commands.getstatusoutput(cmd)
    if retcode == 0:
        nodelist = output.split('\n')
    else:
        logging.warning('get hadoop datanodes failed,retcode=%d' % retcode)

    return nodelist

def get_cdb_backup_hosts(conn):
    cursor = conn.cursor()
    hosts = []
    one_week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    sql = "select distinct(backup_host) from tb_backup_task where create_time > '" + one_week_ago +\
            "' and type in ('mydumper', 'mydumper_nolock', 'xtrabackup', 'xtrabackup_nolock')"
    logging.info(sql)
    cursor.execute(sql)
    backup_hosts = cursor.fetchall()
    for bk_host in backup_hosts:
        hosts.append(bk_host[0])
    cursor.close()

    return hosts

def check_cl5_is_installed(host):
    cmd = 'ajs_client_cmd -t 20 "cd /usr/local/services/cl5/l5_for_qcloud-1.0/bin; ./p.sh | wc -l" ' + host
    logging.info(cmd)
    retcode, output = commands.getstatusoutput(cmd)
    if retcode == 0:
        try:
            count = int(output.rstrip())
            print "process count:%s" % count
            if count == 3:
                return True
        except ValueError:
            return False
    else:
        return False


# any devices which failed to install upload tools is recorded in file 'install_upload_tools_failed_dev.list'
def install_upload_tools_to_backup_hosts(backup_hosts):
    global WEB_HOST
    if len(backup_hosts) == 0:
        return 1

    success = True
    file = open('install_upload_tools_failed_dev.list', 'w')
    for node in backup_hosts:
        # scp cdb2cos.tar.gz to backup host
        src_path = os.path.join(os.getcwd(), "cdb2cos.tar.gz")
        cmd = "ajs_client_scp " + WEB_HOST + " " + src_path + " " + node + " /data "
        logging.info(cmd)
        ret = subprocess.call(cmd, shell=True)
        if ret != 0:
            logging.warning('Failed to copy cdb2cos tool to backup host %s' % node)
            file.write(node)
            success = False
            continue
        else:
            logging.info('Copy cdb2cos tool to %s success' % node)

        # unpack cdb2cos.tar.gz
        cmd = 'ajs_client_cmd -t 600 "cd /data; tar -zxf cdb2cos.tar.gz" ' + node
        logging.info(cmd)
        ret = subprocess.call(cmd, shell=True)
        if ret != 0:
            logging.warning('Failed to unpack cdb2cos.tar.gz on backup host %s' % node)
            file.write(node)
            success = False
            continue
        else:
            logging.info('Unpack cdb2cos tool on %s success' % node)

        if check_cl5_is_installed(node) == True:
            logging.info("Cl5 is already install to backup host %s" % node)
            continue

        # scp cl5_bundle.tar.gz to backup host
        src_path = os.path.join(os.getcwd(), "cl5_bundle.tar.gz")
        cmd = "ajs_client_scp " + WEB_HOST + " " + src_path + " " + node + " /data "
        logging.info(cmd)
        ret = subprocess.call(cmd, shell=True)
        if ret != 0:
            logging.warning('Failed to copy cl5_bundle.tar.gz to backup host %s' % node)
            file.write(node)
            success = False
            continue
        else:
            logging.info('Copy cl5_bundle.tar.gz to %s success' % node)

        # install cl5_bundle on backup host
        cmd = 'ajs_client_cmd -t 600 "tar -zxf /data/cl5_bundle.tar.gz -C /data/; cd /data/cl5_bundle/; sh install.sh" ' + node
        logging.info(cmd)
        ret = subprocess.call(cmd, shell=True)
        if ret != 0:
            logging.warning('Failed to install cl5_bundle on %s' % node)
            file.write(node)
            success = False
            continue
        else:
            logging.info('Install cl5_bundle on backup host %s success' % node)

        file.close()

    return 0 if success == True else 1

def transfer_backup_type(backup_type):
    res_type = ''
    if backup_type == 'xtrabackup' or backup_type == 'xtrabackup_nolock':
        res_type = 'xtrabackup_apply'       #because the redolog in backup is already applied
    elif backup_type == 'hadoop' or backup_type == 'hadoop_nolock':
        res_type = 'mysqldump'
    elif backup_type == 'mydumper' or backup_type == 'mydumper_nolock':
        res_type = 'mydumper'
    else:
        print 'Unknown backup type'

    return res_type

def build_data_backup_storage_path(create_time, job_id, app_name, instance_id,
        instance_name, backup_type, auto_delete, job_admin):
    suffix = ""
    if backup_type in ('xtrabackup', 'xtrabackup_nolock', 'hadoop', 'hadoop_nolock'):
        suffix = ".xb"
    else:
        suffix = ""

    create_date_str = create_time.strftime('%Y-%m-%d')
    create_time_str = create_time.strftime('%Y%m%d%H%M%S')
    delete_way = "manual-delete"
    backup_way = "manual"
    target_type = ""

    if job_admin == "SYSTEM":
        backup_way = "automatic"

    if auto_delete == True:
        delete_way = "automatic-delete"

    target_type = transfer_backup_type(backup_type)

    return "%s/%s/%s/%s/%s/%s/%s/%s/%s/%s_%s_%s%s" % (app_name, "mysql", instance_id, "data", delete_way, create_date_str,
            backup_way, target_type, job_id, instance_name, "backup", create_time_str, suffix)

def build_full_backup_path(mod_id, cmd_id, storage_host, storage_path):
    bucket_url = "%d:%d:%s" % (mod_id, cmd_id, storage_host)
    return "%s|%s|%s" % ("cos", bucket_url, storage_path)

def get_finished_backups(conn):
    cursor = conn.cursor()
    # one_week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    sql = "select bt.id, bt.app_id, bt.app_name, ai.instance_name, bt.backup_host, bt.type, bt.create_time, bt.path "\
            "from tb_app_inst as ai left join tb_backup_task as bt on ai.instance_id = bt.app_id left join tmp_cos_upload_task as ut on bt.id = ut.id "\
            "where bt.status='FINISHED' and bt.delete_flag in ('auto', 'manual') and bt.path not like '%cos|%' "\
            "and (ut.id is null or (ut.status='FAILED' and ut.retry_count < 3)) and "\
            "bt.type in ('hadoop', 'hadoop_nolock', 'mydumper', 'mydumper_nolock', 'xtrabackup', 'xtrabackup_nolock')"

    sql = sql + " order by bt.id desc"
    logging.info(sql)
    cursor.execute(sql)
    backups = cursor.fetchall()
    cursor.close()

    return backups

def process_backup(conn, backup):
    job_id = backup[0]
    instance_id = backup[1]
    app_name = backup[2]
    instance_name = backup[3]
    backup_host = backup[4]
    type = backup[5]
    create_time = backup[6]
    path = backup[7]

    # convert [string] time to [int] timestamp
    timestamp = int(time.mktime(create_time.timetuple()))

    cursor = conn.cursor()
    sql = "UPDATE tmp_cos_upload_task SET status='RUNNING' where id = %d" % job_id
    logging.info(sql)
    cursor.execute(sql)
    conn.commit()

    if type in ('hadoop', 'hadoop_nolock'):
        ret = migrate_hadoop_backup_data(job_id, instance_id, app_name, instance_name, "mysqldump", timestamp, backup_host)
    elif type in ('mydumper', 'mydumper_nolock'):
        ret = migrate_cdb_backup_data(job_id, instance_id, app_name, instance_name, "mydumper", timestamp, backup_host, path)
    elif type in ('xtrabackup', 'xtrabackup_nolock'):
        ret = migrate_cdb_backup_data(job_id, instance_id, app_name, instance_name, "xtrabackup_apply", timestamp, backup_host, path)
    else:
        logging.warning('backup type %s not supported' % type)
        ret = 1

    time.sleep(random.randint(0, 10) * 0.1)

    if ret == 0:
        cos_path = build_data_backup_storage_path(create_time, job_id, app_name, instance_id, instance_name, type, True, 'SYSTEM')
        new_path = build_full_backup_path(MOD_ID, CMD_ID, BUCKET_HOST, cos_path)
        if type in ('mydumper', 'mydumper_nolock'):
            sql = "UPDATE tmp_cos_upload_task ut, tb_backup_task bt SET ut.status='FINISHED',ut.end_time=NOW(),ut.path='%s',ut.new_size=bt.size WHERE ut.id=%d AND bt.id=ut.id" % (new_path, job_id)
        else:
            remote_cmd = "cat /data/cdb2cos/log/" + build_backup_jobid(CLUSTER_ID, job_id) + ".result | grep size"
            cmd = "ajs_client_cmd -t 864000 '" + remote_cmd + "' " + backup_host
            logging.info(cmd)
            retcode, output = commands.getstatusoutput(cmd)
            if retcode == 0:
                size = int(output.rstrip().split(":")[1])
                sql = "UPDATE tmp_cos_upload_task SET status='FINISHED', end_time=NOW(), path = '%s', new_size = %d WHERE id = %d" % (new_path, size, job_id)
            else:
                sql = "UPDATE tmp_cos_upload_task SET status='FAILED', retry_count=retry_count+1 where id = %d" % job_id
    else:
        sql = "UPDATE tmp_cos_upload_task SET status='FAILED', retry_count=retry_count+1 where id = %d" % job_id

    cursor = conn.cursor()
    logging.info(sql)
    cursor.execute(sql)
    conn.commit()

    return ret

def build_backup_jobid(cluster_id, job_id):
    return "bk_%s_%d" % (cluster_id, job_id)

def build_cdb2cos_params(job_id, instance_id, app_name, instance_name, backup_type, create_time):
    params = []
    backup_job_id = build_backup_jobid(CLUSTER_ID, job_id)
    base_dir = "/data/cdb2cos"
    params.append(os.path.join(base_dir, "bin", "cdb2cos"))
    params.append("--op=backup")
    params.append("--cluster-id="+str(CLUSTER_ID))
    params.append('--app-name="'+app_name+'"')
    params.append("--backup-threads=8")
    params.append("--backup-type="+backup_type)
    params.append("--compress-threads=8")
    params.append("--create-time="+str(create_time))
    params.append("--instance-id="+instance_id)
    params.append('--instance-name="'+instance_name+'"')
    params.append("--job-id="+str(job_id))
    params.append("--log-file="+os.path.join(base_dir, "log", backup_job_id+".log"))
    params.append("--exit-message-file="+os.path.join(base_dir, "log", backup_job_id+".result"))

    return params

def migrate_cdb_backup_data(job_id, instance_id, app_name, instance_name, backup_type, create_time, backup_host, path):
    params = build_cdb2cos_params(job_id, instance_id, app_name, instance_name, backup_type, create_time)
    params.append("--backup-data-dir=" + path)
    remote_cmd = ' '.join(params)
    cmd = "ajs_client_cmd -t 864000 '" + remote_cmd + "' " + backup_host
    logging.info(cmd)
    ret = subprocess.call(cmd, shell=True)
    if ret != 0:
        logging.warning('Failed to migrate cdb backup data for %d' % job_id)
        return 1
    else:
        logging.info('Migrate cdb backup data for %d success' % job_id)

    return 0

def migrate_hadoop_backup_data(job_id, instance_id, app_name, instance_name, backup_type, create_time, backup_host):
    params = build_cdb2cos_params(job_id, instance_id, app_name, instance_name, backup_type, create_time)
    params.append("--hadoop-cluster-name=" + HADOOP_CLUSTER_NAME)

    # upload backup data
    remote_cmd = ' '.join(params)
    cmd = "ajs_client_cmd -t 864000 '" + remote_cmd + "' " + backup_host
    logging.info(cmd)
    ret = subprocess.call(cmd, shell=True)
    if ret != 0:
        logging.warning('Failed to migrate hadoop backup data for %d' % job_id)
        return 1
    else:
        logging.info('Migrate hadoop backup data for %d success' % job_id)

    return 0

# result dict -----> key : backup_host, value : a list of backups once backuped on this host
def build_backup_dict(backups):
    bk_dict = dict()
    for bk in backups:
        host = bk[4]
        if host not in bk_dict:
            bk_dict[host] = []
        bk_dict[host].append(bk)

    return bk_dict

def check_items_empty(backup_dict):
    empty = True
    for k, v in backup_dict.iteritems():
        if len(v) != 0:
            empty = False

    return empty

def check_record_in_tmp_table(conn, job_id):
    cursor = conn.cursor()
    sql = "SELECT * FROM tmp_cos_upload_task WHERE id = %d" % job_id
    logging.info(sql)
    cursor.execute(sql)
    record = cursor.fetchall()
    cursor.close()

    return True if len(record) == 1 else False

class Producer(Thread):
    def __init__(self, queue_dict):
        Thread.__init__(self)
        self.queue_dict = queue_dict

    def run(self):
        while True:
            conn = get_db_connection()
            backups = get_finished_backups(conn)
            remaining = len(backups)
            logging.info("===============================length of  backups:%d=======================" % len(backups))

            if remaining <= 0:
                for k, v in self.queue_dict.iteritems():
                    logging.info("Trying to put sentinel object to %s" % k)
                    v.put(sentinel)

                logging.info("We have uploaded all backups")
                return

            backup_dict = build_backup_dict(backups)
            cursor = conn.cursor()
            while not check_items_empty(backup_dict):
                for k, v in backup_dict.copy().iteritems():
                    logging.info("number of items (%d) in backup list %s" % (len(v), k))
                    if k not in self.queue_dict:
                        logging.warning("Attention: backup is in FINISHED status, but backup host %s is not reachable" % k)
                        del backup_dict[k]
                        continue

                    queue = self.queue_dict[k]
                    if len(v) == 0:
                        logging.info("All of backups in %s are uploaded" % k)
                        continue

                    # get the top backup in the backup list
                    head = v[0]
                    try:
                        logging.info("Trying to put %d to queue %s" % (head[0], k))
                        queue.put_nowait(head)
                    except Queue.Full:
                        logging.warning("Failed to put %d to its binding queue %s" % (head[0], k))
                        time.sleep(1)
                        continue

                    v.remove(head)
                    remaining = remaining - 1
                    logging.info("Put backup %d to queue %s success, remaining = %d" % (head[0], k, remaining))
                    # check if the record is already in the tmp table
                    if check_record_in_tmp_table(conn, head[0]) == False:
                        sql = "INSERT INTO tmp_cos_upload_task(id, type, status, start_time) VALUES (" + str(head[0]) +\
                                ", '" + head[5] + "', 'WAITING', NOW())"
                    else:
                        sql = "UPDATE tmp_cos_upload_task SET status='WAITING' WHERE id=%d" % head[0]
                    logging.info(sql)
                    cursor.execute(sql)
                    conn.commit()

                    time.sleep(random.randint(0, 10) * 0.1)
                    logging.info("take a snap and go on")

            logging.info("we gonna sleep %ds and then check if all backups have been uploaded" % DB_CHECK_INTERVAL)
            time.sleep(DB_CHECK_INTERVAL)

class Consumer(Thread):
    def __init__(self, backup_host, queue):
        Thread.__init__(self)
        self.backup_host = backup_host
        self.queue = queue

    def run(self):
        global NUM_OF_CONSUMERS
        ret = 0

        while True:
            conn = get_db_connection()
            time.sleep(1)   # delay consuming items from queue
            data = self.queue.get()
            if data is sentinel:
                self.queue.put(sentinel)    # pass this sentinel to next consumer
                logging.info("The queue of backup host %s is now empty" % self.backup_host)
                lock.acquire()
                NUM_OF_CONSUMERS = NUM_OF_CONSUMERS + 1
                lock.release()
                break
            else:
                ret = process_backup(conn, data)
            
            self.queue.task_done()

def handle_dangling_records(conn):
    cursor = conn.cursor()
    sql = "UPDATE tmp_cos_upload_task SET status='FAILED' where status='RUNNING' or status='WAITING'"
    logging.info(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()

def cleanup(conn, hosts):
    handle_dangling_records(conn)
    for host in hosts:
        cmd = "ajs_client_cmd -t 600 'killall cdb2cos' " + host
        logging.info(cmd)
        ret = subprocess.call(cmd, shell=True)
        if ret != 0:
            logging.warning("Failed to killall cdb2cos in %s" % host)
        else:
            logging.info("killall cdb2cos in %s success" % host)

if __name__ == '__main__':
    install_tools = True
    if len(sys.argv) == 2:
        try:
            flag = int(sys.argv[1])
        except ValueError:
            print 'the install_tools flag must be integer'
            sys.exit()
        
        if flag == 0:
            install_tools = False

    get_oss_metadata()
    parse_cos_conf_file()
    conn = get_db_connection()
    logfile_name = 'BACKUP_MIGRATION.log'
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%F %H:%M:%S',
                filename=logfile_name,
                filemode='w')

    # create tmp table for upload tasks
    create_tmp_table(conn)
    # in the first place, we should handle the dangling records(RUNNING/WAITING) left by previous runs
    handle_dangling_records(conn)

    hosts = set()
    datanodes = get_hadoop_datanodes()
    cdb_backup_hosts = get_cdb_backup_hosts(conn)
    if len(datanodes) == 0 or len(cdb_backup_hosts) == 0:
        print "Failed to get hadoop datanodes or cdb backup hosts"
        sys.exit()
    hosts = set(datanodes).union(set(cdb_backup_hosts))
    logging.info("All of the hadoop backup hosts: %s" % datanodes)
    logging.info("All of the cdb backup hosts: %s" % cdb_backup_hosts)

    # scp uploading tools to all of the hadoop datanodes and cdb backup hosts
    if install_tools == True:
        ret = install_upload_tools_to_backup_hosts(hosts)
        if ret != 0:
            print "Failed to scp upload tools to backup hosts. Please check the failed dev file and handle them properly"
            sys.exit()

    hadoop_consumer_count = len(datanodes) * HADOOP_MAX_JOB_PER_NODE
    queue_dict = dict()
    # start all hadoop consumers
    for host in datanodes:
        queue = Queue.Queue(HADOOP_MAX_JOB_PER_NODE)
        queue_dict[host] = queue

        for i in range(HADOOP_MAX_JOB_PER_NODE):
            consumer = Consumer(host, queue)
            consumer.setDaemon(True)
            consumer.start()

    # start all cdb consumers
    cdb_consumer_count = len(cdb_backup_hosts) * CDB_MAX_JOB_PER_NODE
    for host in cdb_backup_hosts:
        queue = Queue.Queue(CDB_MAX_JOB_PER_NODE)
        queue_dict[host] = queue
        for i in range(CDB_MAX_JOB_PER_NODE):
            consumer = Consumer(host, queue)
            consumer.setDaemon(True)
            consumer.start()

    # start producer
    producer = Producer(queue_dict)
    producer.setDaemon(True)
    producer.start()

    try:
        while True:
            hour_of_day = datetime.datetime.now().hour
            if NUM_OF_CONSUMERS == hadoop_consumer_count + cdb_consumer_count or\
                    hour_of_day < 8:       #we assume that it is safe to migrate data later than 08:00am, this might be properly tuned
                cleanup(conn, hosts)
                break
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        cleanup(conn, hosts)

