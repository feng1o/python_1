#!/usr/bin/python
# encoding:utf-8
import os
import sys
import logging
import time
import random
import math
import subprocess
from threading import Thread, Event, Lock
import mysql.connector
import commands
import Queue

CLUSTER_ID = 0
DB_HOST = ""
DB_PORT = 0
WEB_HOST = ""
SAMPLE_PROPOTION = 0.05     # sample 5% of total uploaded backups
NUM_OF_CONSUMERS = 0
MAX_JOB_PER_NODE = 3
VERIFY_DIR="/data1/verify_backup"

lock = Lock()
sentinel = object()

def get_db_connection():
    try:
        conn = mysql.connector.connect(host=DB_HOST, user='root', port=DB_PORT, password='', db='cdb2')
    except Exception, e:
        print e
        sys.exit()

    return conn

def pass_conf_line(line):
    str = line.rstrip().split('=')[1]
    str = str.split('?')[0]
    str = str.replace("\"", '').strip()
    return str

def get_oss_metadata():
    global CLUSTER_ID,DB_HOST,DB_PORT,HADOOP_CLUSTER_NAME,WEB_HOST
    with open('/usr/local/cdb_mtnc/install/base.conf', 'r') as f:
        for line in f:
            if 'set:default_clusterid=' in line:
                CLUSTER_ID = pass_conf_line(line)
            elif 'set:db_host=' in line:
                DB_HOST = pass_conf_line(line)
            elif 'set:db_port=' in line:
                DB_PORT = pass_conf_line(line)
            elif 'set:cdb_web_ip=' in line:
                WEB_HOST = pass_conf_line(line)
            else:
                pass

def create_tmp_table(conn):
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS `tmp_cos_download_task`(`id` int(11) NOT NULL AUTO_INCREMENT, `status` enum('WAITING','RUNNING','FINISHED','FAILED') NOT NULL, "\
            "`start_time` datetime DEFAULT '0000-00-00 00:00:00', `end_time` datetime DEFAULT '0000-00-00 00:00:00', `verify_result` enum('PASSED', 'FAILED'),  "\
            "`type` enum('hadoop','hadoop_nolock','mydumper','mydumper_nolock','xtrabackup','xtrabackup_nolock') NOT NULL, PRIMARY KEY (`id`)) "\
            "ENGINE=InnoDB DEFAULT CHARSET=utf8"
    logging.info(sql)
    cursor.execute(sql)
    cursor.close()

def build_import_jobid(cluster_id, job_id):
    return "im_%s_%d" % (cluster_id, job_id)

def build_tool_params(job_id, backup_type, storage_path):
    params = []
    import_job_id = build_import_jobid(CLUSTER_ID, job_id)
    base_dir = "/data/cdb2cos"
    params.append(os.path.join(base_dir, "bin", "cdb2cos"))
    params.append("--op=import")
    params.append("--job-id="+str(job_id))
    params.append("--cluster-id="+str(CLUSTER_ID))
    params.append("--extract-threads=8")
    params.append("--decompress-threads=8")
    params.append("--backup-type="+backup_type)
    params.append('--storage-path="'+storage_path+'"')
    params.append("--log-file="+os.path.join(base_dir, "log", import_job_id+".log"))
    params.append("--exit-message-file="+os.path.join(base_dir, "log", import_job_id+".result"))
    if backup_type in ('mydumper', 'xtrabackup'):
        params.append("--target-dir="+os.path.join(VERIFY_DIR, import_job_id+"_md5_cos"))

    return params

def get_uploaded_backups(conn):
    cursor = conn.cursor()
    sql = "select ut.id, ut.path, bt.backup_host, bt.type, bt.path from tmp_cos_upload_task ut, tb_backup_task bt "\
            "where bt.id = ut.id and ut.status='FINISHED' and bt.delete_flag in ('auto', 'manual') and "\
            "ut.type in ('hadoop', 'hadoop_nolock', 'mydumper', 'mydumper_nolock', 'xtrabackup', 'xtrabackup_nolock')"

    logging.info(sql)
    cursor.execute(sql)
    backups = cursor.fetchall()
    cursor.close()

    random.shuffle(backups)
    return backups

def build_backup_dict(backups):
    bk_dict = dict()
    for bk in backups:
        host = bk[2]
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
    sql = "SELECT * FROM tmp_cos_download_task WHERE id = %d" % job_id
    logging.info(sql)
    cursor.execute(sql)
    record = cursor.fetchall()
    cursor.close()

    return True if len(record) == 1 else False

def download_backup(conn, job_id, backup_type, backup_host, cos_path):
    params = build_tool_params(job_id, backup_type, cos_path)
    remote_cmd = ' '.join(params)
    cmd = "ajs_client_cmd -t 864000 '" + remote_cmd + "' " + backup_host
    logging.info(cmd)
    ret = subprocess.call(cmd, shell=True)
    if ret != 0:
        logging.warning("Failed to download and calc md5sum for %d", job_id)
    else:
        logging.info("Download and calc md5sum for %d success" % job_id)

    if ret == 0:
        sql = "UPDATE tmp_cos_download_task SET status='FINISHED', end_time=NOW() WHERE id = %d" % (job_id)
    else:
        sql = "UPDATE tmp_cos_download_task SET status='FAILED', end_time=NOW() WHERE id = %d" % (job_id)

    cursor = conn.cursor()
    logging.info(sql)
    cursor.execute(sql)
    conn.commit()

    return ret

def verify_hadoop_backup(conn, job_id, backup_type, backup_host, cos_path):
    ret = download_backup(conn, job_id, backup_type, backup_host, cos_path)
    if ret != 0:
        return 1

    # generate md5 file of the original hadoop backup
    import_job_id = build_import_jobid(CLUSTER_ID, job_id)
    hadoop_path_file = os.path.join(VERIFY_DIR, import_job_id + ".hadoop")
    local_md5_file = os.path.join(VERIFY_DIR, import_job_id + "_md5_local")
    remote_cmd = "cd /data/cdb2cos/checksum; hadoop fs -cat `cat " + hadoop_path_file + "` > " + local_md5_file
    cmd = "ajs_client_cmd -t 864000 '" + remote_cmd + "' " + backup_host
    logging.info(cmd)
    ret = subprocess.call(cmd, shell = True)
    if ret != 0:
        logging.warning("Failed to calc original md5sum for hadoop backup: %d", job_id)
        return 1
    else:
        logging.info("Calc original md5sum for hadoop backup: %d success", job_id)

    # diff two md5 files to check if the original hadoop backup is correctly uploaded
    cos_md5_file = os.path.join(VERIFY_DIR, import_job_id + "_md5_cos")
    remote_cmd = "diff %s %s" % (local_md5_file, cos_md5_file)
    cmd = "ajs_client_cmd -t 864000 '" + remote_cmd + "' " + backup_host
    ret, output = commands.getstatusoutput(cmd)
    if ret == 0 and output == '':
        logging.info("The content in md5sum file for local and cos of %d is the same" % job_id)
        return 0
    else:
        return 1

def verify_cdb_backup(conn, job_id, backup_type, backup_host, cos_path, local_backup_path):
    ret = download_backup(conn, job_id, backup_type, backup_host, cos_path)
    if ret != 0:
        return 1

    # generate md5 dir according to original local backup, in the md5 dir,
    # the file just contains an md5 checksum string instead of its original content
    import_job_id = build_import_jobid(CLUSTER_ID, job_id)
    local_md5_path = os.path.join(VERIFY_DIR, import_job_id + "_md5_local")
    remote_cmd = "cd /data/cdb2cos/bin; sh calc_md5sum.sh %s %s" % (local_backup_path, local_md5_path)
    cmd = "ajs_client_cmd -t 864000 '" + remote_cmd + "' " + backup_host
    logging.info(cmd)
    ret = subprocess.call(cmd, shell=True)
    if ret != 0:
        logging.warning("Failed to calc md5sum of local backup for %d", job_id)
        return 1
    else:
        logging.info("Calc md5sum of local backup for %d success" % job_id)

    # diff two md5 directories to check if the original backup is correctly uploaded
    cos_md5_path = os.path.join(VERIFY_DIR, import_job_id + "_md5_cos")
    remote_cmd = "diff -r %s %s" % (local_md5_path, cos_md5_path)
    cmd = "ajs_client_cmd -t 864000 '" + remote_cmd + "' " + backup_host
    ret, output = commands.getstatusoutput(cmd)
    if ret == 0 and output == '':
        logging.info("The content in md5sum directory for local and cos is the same")
        return 0
    else:
        logging.info("The content in md5sum directory for local and cos is probably different")
        return 1

def extract_storage_path(path):
    lst = path.split('|')
    res = ""
    if len(lst) != 3:
        logging.warning("Invalid cos path: %s" % path)
    else:
        res = lst[2]

    return res

def verify_backup(conn, backup):
    job_id = backup[0]
    cos_path = extract_storage_path(backup[1])
    backup_host = backup[2]
    type = backup[3]
    local_path = backup[4]

    cursor = conn.cursor()
    sql = "UPDATE tmp_cos_download_task SET status='RUNNING' where id = %d" % job_id
    logging.info(sql)
    cursor.execute(sql)
    conn.commit()

    if type in ('hadoop', 'hadoop_nolock'):
        ret = verify_hadoop_backup(conn, job_id, "mysqldump", backup_host, cos_path)
    elif type in ('mydumper', 'mydumper_nolock'):
        ret = verify_cdb_backup(conn, job_id, "mydumper", backup_host, cos_path, local_path)
    elif type in ('xtrabackup', 'xtrabackup_nolock'):
        ret = verify_cdb_backup(conn, job_id, "xtrabackup", backup_host, cos_path, local_path)
    else:
        logging.warning("backup type %s is not supported" % type)
        ret = 1

    time.sleep(random.randint(0, 10) * 0.1)
    if ret == 0:
        sql = "UPDATE tmp_cos_download_task SET verify_result='PASSED' WHERE id = %d" % (job_id)
    else:
        sql = "UPDATE tmp_cos_download_task SET verify_result='FAILED' WHERE id = %d" % (job_id)
    cursor = conn.cursor()
    logging.info(sql)
    cursor.execute(sql)
    conn.commit()

    return ret

class Producer(Thread):
    def __init__(self, backups, queue_dict):
        Thread.__init__(self)
        self.backups = backups
        self.queue_dict = queue_dict

    def run(self):
        conn = get_db_connection()
        backup_dict = build_backup_dict(self.backups)
        cursor = conn.cursor()
        while not check_items_empty(backup_dict):
            for k, v in backup_dict.copy().iteritems():
                logging.info("number of items (%d) in backup list %s" % (len(v), k))
                if k not in self.queue_dict:
                    logging.warning("Attention: backup is uploaded to cos, but its original backup host %s is not reachable now" % k)
                    del backup_dict[k]
                    continue

                queue = self.queue_dict[k]
                if len(v) == 0:
                    logging.info("All of the sampled backups in %s are downloaded" % k)
                    try:
                        queue.put_nowait(sentinel)
                    except Queue.Full:
                        logging.warning("Failed to put sentinel to queue %s" % k)
                    continue

                # get the top uploaded backup in the backup list
                head = v[0]
                try:
                    logging.info("Trying to put %d to queue %s" % (head[0], k))
                    queue.put_nowait(head)
                except Queue.Full:
                    logging.warning("Failed to put %d to its binding queue %s" % (head[0], k))
                    continue

                v.remove(head)
                logging.info("Put uploaded backup %d to its binding queue %s success" % (head[0], k))
                # check if the record is already in the tmp table
                if check_record_in_tmp_table(conn, head[0]) == False:
                    sql = "INSERT INTO tmp_cos_download_task(id, type, status, start_time) VALUES (" + str(head[0]) +\
                            ", '" + head[3] + "', 'WAITING', NOW())"
                else:
                    sql = "UPDATE tmp_cos_download_task SET status='WAITING' WHERE id=%d" % head[0]

                logging.info(sql)
                cursor.execute(sql)
                conn.commit()

                time.sleep(random.randint(0, 10) * 0.1)

class Consumer(Thread):
    def __init__(self, backup_host, queue):
        Thread.__init__(self)
        self.backup_host = backup_host
        self.queue = queue

    def run(self):
        global NUM_OF_CONSUMERS

        while True:
            conn = get_db_connection()
            time.sleep(1)
            data = self.queue.get()
            if data is sentinel:
                self.queue.put(sentinel)
                logging.info("The queue of %s backup is now empty" % self.backup_host)
                lock.acquire()
                NUM_OF_CONSUMERS = NUM_OF_CONSUMERS + 1
                lock.release()
                break
            else:
                ret = verify_backup(conn, data)
            
            self.queue.task_done()

def get_hosts_from_backup(backups):
    backup_hosts = set()
    for bk in backups:
        host = bk[2]
        backup_hosts.add(host)

    return backup_hosts

def handle_dangling_records(conn):
    cursor = conn.cursor()
    sql = "UPDATE tmp_cos_download_task SET status='FAILED' where status='RUNNING' or status='WAITING'"
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
    get_oss_metadata()
    conn = get_db_connection()
    logfile_name = "BACKUP_VERIFICATION.log"
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%F %H:%M:%S',
                filename=logfile_name,
                filemode='w')
    # create tmp table for download tasks
    create_tmp_table(conn)
    # in the first place, we should handle the dangling records(RUNNING/WAITING) left by previous runs
    handle_dangling_records(conn)

    backup_hosts = set()
    uploaded_backups = get_uploaded_backups(conn)
    sample_number = int(math.ceil(len(uploaded_backups) * SAMPLE_PROPOTION))
    if sample_number > 0:
        sample_backups = uploaded_backups[:sample_number]
        backup_hosts = get_hosts_from_backup(sample_backups)
        logging.info("All of the backup hosts in the sampled backups: %s" % backup_hosts)
    else:
        logging.info("No need to verify backups")

    consumer_count = len(backup_hosts) * MAX_JOB_PER_NODE
    queue_dict = dict()
    # start all consumers
    for host in backup_hosts:
        queue = Queue.Queue(MAX_JOB_PER_NODE)
        queue_dict[host] = queue
        for i in range(MAX_JOB_PER_NODE):
            consumer = Consumer(host, queue)
            consumer.setDaemon(True)
            consumer.start()

    producer = Producer(sample_backups, queue_dict)
    producer.setDaemon(True)
    producer.start()

    try:
        while True:
            hour_of_day = datetime.datetime.now().hour
            if NUM_OF_CONSUMERS == consumer_count or hour_of_day < 8:
                cleanup(conn, hosts)
                break
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        cleanup(conn, hosts)

