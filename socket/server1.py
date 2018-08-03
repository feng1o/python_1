"""
#Echo server program
import socket
 
HOST="127.0.0.1"  #空代表0.0.0.0
PORT= 50007  #监听端口
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 生成socket tcp通信实例，
s.bind((HOST,PORT)) #绑定ip和端口，注意bind只接受一个参数，(HOST,PORT) 做成一个元祖传进去
s.listen(1)  #开始监听，里面的数字是代表服务端在拒绝新连接之前可以最多挂起多少连接，不过实验过了没啥用，所以写个1就好了
while True:
	conn,addr= s.accept()  #接受连接，并返回两个变量，conn代表每个新连接进入后服务端都会为其生成一个新实例，后面可以用这个实例进行发送和接收，addr是连接进来的客户端的地址，accept()方法在有新连接进入时就会返回conn,addr这两个变量，但如果没有连接时，此方法就会阻塞直至有新连接过来。
	print('Connected by', addr)
	while  True:
		data = conn.recv(1024) #接收1024字节数据
		if not data: break     #如果收不到客户端数据了（代表客户端断开了），就断开
		conn.sendall(data.upper())    #将收到的数据全变成大写再发给客户端
     
conn.close() #关闭连接"""

import socket
from time import ctime

HOST = "127.0.0.1"  # 空代表0.0.0.0
PORT = 50007  # 监听端口
BUFFSIZE = 1024
HEAD_LEN = 4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 生成socket tcp通信实例，
s.bind((HOST, PORT))  # 绑定ip和端口，注意bind只接受一个参数，(HOST,PORT) 做成一个元祖传进去
s.listen(1)  # 开始监听，里面的数字是代表服务端在拒绝新连接之前可以最多挂起多少连接，不过实验过了没啥用，所以写个1就好了
while True:
    conn, addr = s.accept()  # 接受连接，并返回两个变量，conn代表每个新连接进入后服务端都会为其生成一个新实例，后面可以用这个实例进行发送和接收，addr是连接进来的客户端的地址，accept()方法在有新连接进入时就会返回conn,addr这两个变量，但如果没有连接时，此方法就会阻塞直至有新连接过来。
    print('Connected by', addr)
    while True:
        data = conn.recv(BUFFSIZE).decode()  # 接收1024字节数据
        print("recived data is: %s...%d " % (data, len(data)))
        if not data:
            print("closed...")
            # break   # 如果收不到客户端数据了（代表客户端断开了），就断开
        # 将收到的数据全变成大写再发给客户端
        conn.sendall(('[%s] %s' % (ctime(), data)).encode())
conn.close()  # 关闭连接
