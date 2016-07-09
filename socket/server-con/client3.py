import socket
import time
import sys

print("sys.stdin...%s" % sys.stdin)
print(sys.stdin.fileno())
a = 3
def fun1():
	global a
	print(a)
	a = 1
	pass
print("....%d" % a)
print(time.ctime())
# create a socket and connect to a server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))

# send and receive some data
sock.sendall(b'test')
data = sock.recv(1024)
print(data.decode())