class LogSignleton(object):
    def __init__(self,log_config):
        '''单例模式'''
        pass

    def __new__(cls,log_config):

        mutex = threading.Lock()
        mutex.acquire() #上锁,防止多线程下出问题
        if not hasattr(cls,'instance'):
            cls.instance = super(LogSignleton,cls).__new__(cls)
            cls.instance.log_filename = read_config(log_config,'logger','log_file')
            if cls.instance.log_filename is not None: # 判断是否为目录
                try:
                    # 返回的是文件名,不包括前面的路径
                    filename = os.path.basename(cls.instance.log_filename)
                    # 返回的是目录名,不包括文件名
                    filepath = os.path.dirname(cls.instance.log_filename)
                    print filepath
                    # splitext:分离文件名和后缀 split:分离文件路径和文件
                    parent_path, ext = os.path.splitext(filename)
                    # 定义时间显示格式
                    tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
                    # 重新组装日志文件名
                    filename = parent_path + '_' + tm + ext
                    cls.instance.log_filename = filepath + '/' + filename
                except Exception:
                    raise
            cls.instance.max_bytes_each = int(read_config(log_config,'logger','max_bytes_each'))
            cls.instance.backup_count = int(read_config(log_config,'logger','backup_count'))
            cls.instance.format = read_config(log_config,'logger','format')
            cls.instance.log_level_in_console = int(read_config(log_config,'logger','log_level_in_console'))
            cls.instance.log_level_in_logfile = int(read_config(log_config,'logger','log_level_in_logfile'))
            cls.instance.logger_name = read_config(log_config,'logger','logger_name')
            cls.instance.console_log_on = int(read_config(log_config,'logger','console_log_on'))
            cls.instance.logfile_log_on = int(read_config(log_config,'logger','logfile_log_on'))
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release() #释放锁
        return cls.instance

    def get_logger(self):
        return self.logger


    def __config_logger(self):
        fmt = self.format.replace('|','%')
        formatter = logging.Formatter(fmt)
        if self.console_log_on == 1: #如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.setLevel(self.log_level_in_console)

        if self.logfile_log_on == 1: #如果开启文件日志
            rt_file_handler = RotatingFileHandler(self.log_filename,maxBytes=self.max_bytes_each,backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)
            self.logger.setLevel(self.log_level_in_logfile)