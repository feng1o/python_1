# This is for a system with little memory (<= 64M) where MySQL is only used
[client]
port		= <?cs var:port?>
socket		= /tmp/mysql_<?cs var:port?>.sock

[mysqld]
port		= <?cs var:port?>
socket		= /tmp/mysql_<?cs var:port?>.sock
pid-file    = <?cs var:data_dir?>/Tencent64.pid
datadir     = <?cs var:data_dir?>
slow_query_log_file = <?cs var:data_dir?>/slow_query.log
tmpdir = <?cs var:tmp_dir?>
slave_load_tmpdir = <?cs var:tmp_dir?>

#Tencent root user configuration file
tencent-root-cnf = <?cs var:data_dir?>/tmy.conf

secure_file_priv = <?cs var:data_dir?>

#general-log = 1
slow_query_log = 1
max_connect_errors=999999999

skip-external-locking
skip-name-resolve

performance_schema = OFF

<?cs if:gtid == "YES" ?>
#gtid
gtid_mode=ON
enforce-gtid-consistency

#_FOR_SEMI_SYNC_
plugin-load=semisync_master.so
rpl_semi_sync_master_wait_forever=0
rpl_semi_sync_master_wait_point=AFTER_COMMIT

#WARN:myisam can convert to innodb,but show warnings
myisam_conversion_innodb=WARN
tencent_myisam_conversion_innodb=TRY
<?cs else?>
myisam_conversion_innodb=OFF
tencent_myisam_conversion_innodb=OFF
<?cs /if?>


<?cs if:working_mode =="YES" ?>
#working_mode
cdb_working_mode_enabled=OFF
cdb_working_mode_default=READWRITE
<?cs /if?>


#compatible MySQL5.1
binlog_checksum = crc32
key_buffer_size = 16M
max_allowed_packet = 1G
table_open_cache = 2000
sort_buffer_size = 512K
net_buffer_length = 8K
read_buffer_size = 256K
read_rnd_buffer_size = 512K
myisam_sort_buffer_size = 8M
thread_stack = 128K
query_cache_size = 0M
query_cache_type = 0      #must be chanaged with query_cache_size, and reboot mysqld

innodb_log_group_home_dir = <?cs var:log_dir?>

#for master-slave
server-id	= <?cs var:server_id?> 
log-bin = <?cs var:log_dir?>/mysql-bin
relay-log = <?cs var:log_dir?>/relay-bin
log-slave-updates
binlog_format = row 
binlog_row_image = minimal
#master-host = 
#master-user = root
#master-password    = 
#master-port        = <?cs var:port?>
innodb_log_buffer_size = 64M
#replicate-ignore-db=mysql

#{_REPLICATE_DO_TABLE_}
#{_REPLICATE_WILD_TABLE_}

#thread_cache_size = 64
log_bin_trust_function_creators = 1
thread_stack = 512K
innodb_file_per_table = 1
innodb_lock_wait_timeout=7200
open_files_limit=102400
<?cs set:max_connections = buf_size / #5 ?>
<?cs if:max_connections > 10240 ?> <?cs set:max_connections = 10240 ?> <?cs /if?>
<?cs if:max_connections < 800 ?> <?cs set:max_connections = 800 ?> <?cs /if?>
max_connections= <?cs var:max_connections?>
<?cs set:tmp_table_size = buf_size / #5 ?>
<?cs if:tmp_table_size > 1024 ?> <?cs set:tmp_table_size = 1024 ?> <?cs /if?>
tmp_table_size= <?cs var:tmp_table_size?>M
innodb_buffer_pool_size = <?cs var:buf_size?>M
#innodb_additional_mem_pool_size = 64M (deprecated from 5.6.3)
<?cs set:log_size = (buf_size / #25000 + 1) * 512 ?>
innodb_log_file_size =  <?cs var:log_size?>M
innodb_flush_log_at_trx_commit=2
innodb_io_capacity=20000
innodb_flush_method = O_DIRECT
innodb_file_format=Barracuda
innodb_file_format_max=Barracuda
innodb_open_files=1024
innodb_strict_mode=1
innodb_purge_threads=1
innodb_read_io_threads = 12
innodb_write_io_threads = 12
cdb_slave_lock_optimization = ON
rpl_semi_sync_io_optimization_enabled = off
cdb_enable_offset_pushdown = off
extra_port = 54321
extra_max_connections = 20
thread_pool_idle_timeout = 60
thread_pool_oversubscribe = 3
thread_pool_size = 48
thread_pool_stall_limit = 500
thread_pool_max_threads = MAX_CONNECTIONS
thread_pool_high_prio_tickets = UINT_MAX
thread_pool_high_prio_mode = TP_HIGH_PRIO_MODE_TRANSACTI
threadpool_workaround_epoll_bug = 1
cdb_forbid_mysql_write = TRUE
innodb_async_drop_tmp_dir = NULL
innodb_async_truncate_size = 128
innodb_cdb_log_checksum_algorithm = crc32
slave_net_timeout = 32
core_file  = on
innodb_print_all_deadlocks = on
innodb_purge_threads  = 4
master_info_repository = table
relay_log_info_repository = table
table_open_cache_instances = 16
innodb_buffer_pool_instances = 16
innodb_flush_neighbors = 0
innodb_thread_concurrency = 32

table_definition_cache= 768
thread_cache_size = 512
interactive_timeout=3600  
wait_timeout=3600
log_timestamps = system

read_only = <?cs if:inst_type=="slave" || inst_type=="ro_slave"?>1<?cs else?>0<?cs /if?>

<?cs include:"my_cnf_5_7_18.custom" ?>

!include <?cs var:data_dir?>/your.cnf
!include <?cs var:data_dir?>/her.cnf
[mysqldump]
quick
max_allowed_packet = 16M

[mysql]
no-auto-rehash
# Remove the next comment character if you are not familiar with SQL
#safe-updates

[myisamchk]
key_buffer_size = 20M
sort_buffer_size = 20M
read_buffer = 2M
write_buffer = 2M

[mysqlhotcopy]
interactive-timeout

[mysqld_safe]
core-file-size=unlimited
