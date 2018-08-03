
import socket
import base64
import sys
import os
import time


#HOST = '127.0.0.1'  # 远程socket服务器ip
#HOST = '115.28.159.75'  # 远程socket服务器ip
#HOST = '118.114.229.110'
HOST = '120.25.241.211' 
PORT = 9999        # 远程socket服务器端口

BUFFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket
s.connect((HOST, PORT))  # 连接socket服务器

print(socket.gethostname())
print(socket.gethostbyaddr("127.0.0.1"))
while True:
    # msg = input("Your msg::")  # 让用户输入消息，去除回车和空格
    # msg = input("Your msg::").strip() #让用户输入消息，去除回车和空格
    data = s.recv(4).decode()  # 接收服务器的消息
    print('Received:', data)

    data = s.recv(12).decode()  # 接收服务器的消息
    print('Received:', data)

    msg = '12'
    if len(msg) < 4:
        fix = 4 - len(msg)
        for x in range(0, fix):
            msg = '0' + msg
            print(msg)
        # continue
    # msg = base64.b64encode(msg)  # 发送的是2进制码子？
    s.send(msg.encode('utf-8'))  # 向服务器发送消息
    # s.send("a0001fdg".encode())
    # s.send("abcdefdg".encode())
    if (int)(msg) == 12:
        print('msg...length ok...')
        s.send("987654321000".encode())
    # s.send(str.encode())
    #data = s.recv(BUFFSIZE).decode()  # 接收服务器的消息

    #print('Received:', data)
    time.sleep(1)
    # break
s.close()

if __name__ == '__main__':
    print("oooooo")
