###########################################################################
# Concurrent server>  server.py                                           #
# author: lf                                                              #
# time: 2016-07-10                                                        #
#                                                                         #
###########################################################################
#import convolutional
import test
import errno
import os
import signal
import socket
import readpic
import time
import datetime
import struct
import logging

SERVER_ADDRESS = (HOST, PORT) = '',9999 
REQUEST_QUEUE_SIZE = 1024
HEAD_LEN = 4
#pic_nu = 1

LOG_FILE = 'log'
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
def sig_chldHandler(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return

def handle_request(client_connection, pic_nu):
	while True:
		logger.info("deal client connection\n")
		rHeadLen = recvall(client_connection, struct.calcsize('I'))
		#rHeadLen = client_connection.recv(HEAD_LEN).decode()
#logger.info("read Headlen is:%s" % int(rHeadLen))
		length = struct.unpack('I', rHeadLen)[0]
		print("size ===" + str(length))
		logger.info("read Headlen is:"+ str(length))
#print("read Headlen is:%s" % int(rHeadLen))
#print("read Headlen is:%s" % int(rHeadLen))

		#picBody = client_connection.recv(int(rHeadLen)).decode()
#picBody = recvall(client_connection, int(rHeadLen))
		print("read picbody is ...")
		picBody = recvall(client_connection, length)
#print("read picbody is {picbody}...".format(picbody = picBody))
#		logger.info("read picbody is ...%s"% picBody)
#		print("read picbody is ...%s"% picBody)"""
		logger.info("read picbody is ...")
		cur_path = os.path.abspath('.')
		# global pic_nu 
		pic_nu = pic_nu + 1
		rdpic = readpic.tsf_picFile(cur_path, 'pic' + str(pic_nu) + '.jpg', 'wb+', picBody)
		rdpic.ow_pic()
		#readpic.tsf_picFile.ow_pic(rdpic)
		client_connection.sendall(("test.................").encode())
		# print(request.decode())
		# http_response = b"""\ HTTP/1.1 200 OK  Hello, World! """
		# client_connection.sendall(http_response)

def recvall(sockfd, count):
	buf = b''
	while len(buf) < count:
		nRead = sockfd.recv(count - len(buf))
		if not nRead:
			return None
		buf += nRead
	return buf

def serve_forever():
	listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listen_socket.bind(SERVER_ADDRESS)
	listen_socket.listen(REQUEST_QUEUE_SIZE)
	logger.info('listen on {port} ...'.format(port=PORT))
	print('listen on {port} ...'.format(port=PORT))
	
	signal.signal(signal.SIGCHLD, sig_chldHandler)
	
	while True:
		try:
			client_connection, client_address = listen_socket.accept()
		except IOError as e:
			code, msg = e.args
            # restart 'accept' if it was interrupted
			if code == errno.EINTR:
				continue
			else:
				raise
		
		pid = os.fork()
		if pid == 0:  # child
			listen_socket.close()  # close child copy
			pic_nu = 1
			handle_request(client_connection, pic_nu)
			logger.info("reques over....%s" % os.getpid())
			print("reques over....%s" % os.getpid())
			client_connection.close()
			os._exit(0)
		else:  # parent
			client_connection.close()  # close parent copy and loop over

if __name__ == '__main__':
#	convolutional.fun()
	test.fun()
	serve_forever()

