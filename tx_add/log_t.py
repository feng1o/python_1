import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='log_t.log',
                filemode='w')
    
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')



#################################################################################################
#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler('log_t.log', maxBytes=100,backupCount=2)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)
################################################################################################
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

def log_mod(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fh = logging.FileHandler('access.log',encoding='utf-8')
    fh.setLevel(logging.WARNING)
    ch_formatter = logging.Formatter('%(module)s-%(lineno)d %(levelname)s:%(message)s')
    fh_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s',datefmt='%Y/%m/%d %H:%M:%S')
    ch.setFormatter(ch_formatter)
    fh.setFormatter(fh_formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    # 这里需要把logger返回
    return logger