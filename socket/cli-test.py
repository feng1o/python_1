
import socket


# HOST = '127.0.0.1'  # 远程socket服务器ip
HOST= '115.28.159.75' # 远程socket服务器ip
PORT = 10028         # 远程socket服务器端口

BUFFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket
s.connect((HOST, PORT))  # 连接socket服务器

print(socket.gethostname())
print(socket.gethostbyaddr("127.0.0.1"))
while True:
    # msg = input("Your msg::")  # 让用户输入消息，去除回车和空格
    # msg = input("Your msg::").strip() #让用户输入消息，去除回车和空格
    msg = '0001'
    if len(msg) < 4:
    	fix = 4 - len(msg)
    	for  x in range(0, fix):
    	 	msg ='0' + msg 
    	 	print(msg)
        # continue 
    s.send(msg.encode())  # 向服务器发送消息
    # s.send("a0001fdg".encode())
    # s.send("abcdefdg".encode())
    if (int)(msg) == 1:
    	print('msg...', 1)
    	s.send("1".encode())   
    #s.send(str.encode())
    data = s.recv(BUFFSIZE).decode()  # 接收服务器的消息

    print('Received:', data)
s.close()
