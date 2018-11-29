#!/usr/bin/python
# fileName: strGetName.py

import sys
import os
import copy

tpl_suffix=".tpl"
old_suffix=".old"

param = {
    "cdb_slave_lock_optimization" : "ON",
    "rpl_semi_sync_io_optimization_enabled" : "off",
    "cdb_enable_offset_pushdown" : "off",
    "extra_port" : 54321,
    "extra_max_connections" : 20,
    "thread_pool_idle_timeout" : 60,
    "thread_pool_oversubscribe" : 3,
    "thread_pool_size" : "cpu核数",
    "thread_pool_stall_limit" : 500,
    "thread_pool_max_threads" : "MAX_CONNECTIONS",
    "thread_pool_high_prio_tickets" : "UINT_MAX",
    "thread_pool_high_prio_mode" : "TP_HIGH_PRIO_MODE_TRANSACTI",
    "threadpool_workaround_epoll_bug" : 1,
    "cdb_forbid_mysql_write" : "TRUE",
    "innodb_async_drop_tmp_dir" : "NULL",
    "innodb_async_truncate_size" : 128,
    "innodb_cdb_log_checksum_algorithm" : "crc32",
    "slave_net_timeout" : 32,
    "binlog_checksum" : "crc32",
    "core_file " : "on",
    "innodb_print_all_deadlocks" : "on",
    "innodb_purge_threads " : 4,
    "master_info_repository" : "table",
    "relay_log_info_repository" : "table",
    "table_open_cache_instances" : 16,
    "table_open_cache" : 2000,
    "innodb_buffer_pool_instances" : 16,
    "innodb_flush_neighbors" : 0,
    "innodb_thread_concurrency" : 32
}

new_add_param = {}

def get_new_add_params(file_path):
    global new_add_param 
    new_add_param = copy.deepcopy(param)
    print("new ----------", new_add_param)
    print( id(param), id(new_add_param))
    with open(file_path) as fd:
        line = fd.readline()
        print(line)
        while line:
            for key in param:
                if line.find(key) != -1:
                    print("remove key = ", key)
                    new_add_param.pop(key)
            line = fd.readline()

def rename_files(path):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            rename_files(file_path)
        elif os.path.splitext(file_path)[1] == tpl_suffix:
            os.rename(file_path, os.path.splitext(file_path)[0] + old_suffix)


def get_file_names(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            get_file_names(file_path, list_name)
        elif os.path.splitext(file_path)[1] == old_suffix:
            list_name.append(file_path)
    return list_name

def gen_cnf_file(file_list):
    for item in file_list:
        print("\n\n\n________________________________________________________________")
        print("\t files:")
        print("\t\t ", item)
        print("-------------------",os.path.splitext(item)[0])
        #fd = open(file_name, "r+", encoding="utf-8")
        if item.find("ts85") != -1:
            param["thread_pool_size"] = 24
        else:
            param["thread_pool_size"] = 48
        get_new_add_params(item)
        print(" -----param all = {0}, \n, ------param add = {1}".format(param, new_add_param))
        tpl_fd = open(os.path.splitext(item)[0] + tpl_suffix, "w", encoding='utf-8')
        with open(item) as fd:
            line = fd.readline()
            while line:
                print(line.strip())
                line = check_line(line)
                #print("\t\t new line ={0}".format(line))
                tpl_fd.write(line)
                if line.find("innodb_write_io_threads") >= 0:
                    for key in new_add_param:
                        add_line = key + " = " + str(new_add_param[key]) + "\n"
                        tpl_fd.write(add_line)
                line = fd.readline()
        tpl_fd.close() 


def check_line(line):
    del_key_list = []
    for key in param:
        if line.find(key) != -1:
            print (" --------------找到：",key)
            line = key + " = " + str(param[key]) + "\n"
            del_key_list.append(key)
            print(param)
            print("  --------------new line = ", line)
    #for key in del_key_list:
    #    param.pop(key)
    return line 


if __name__ == '__main__':
    file_list = []
    rename_files(".")
    get_file_names(".", file_list)
    gen_cnf_file(file_list)
    


