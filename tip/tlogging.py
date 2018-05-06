import logging

LOG_FILE = 'logx'
logger = logging.getLogger(LOG_FILE)
logger.setLevel(logging.DEBUG)

# create log file handler
log_path = "./log.log"
log_handler = logging.FileHandler(log_path)
log_handler.setLevel(logging.INFO)

# formate
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S" 
formatter = logging.Formatter(fmt, datefmt)

#add 
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

# log print
logger.info('log info.....')

/**
 * @param  {[type]}
 * @param  {[type]}
 * @return {[type]}
 */
function xx(a,b) {
	return a;
}
def xx(a):
	return a