
import socket
import base64
import sys
import os
import time

''' 发送json训练请求到server'''
# HOST = '127.0.0.1'  # 远程socket服务器ip
HOST = '120.25.241.211'  # 远程socket服务器ip
# HOST = '182.92.10.18'
PORT = 7004        # 远程socket服务器端口

BUFFSIZE = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket
s.connect((HOST, PORT))  # 连接socket服务器

print(socket.gethostname())
print(socket.gethostbyaddr("127.0.0.1"))
Tru = 1
while Tru==1:
    Tru = 2
    # msg = input("Your msg::")  # 让用户输入消息，去除回车和空格
    # msg = input("Your msg::").strip() #让用户输入消息，去除回车和空格
    #keepOnstr = "000000000079{\"Content-Length\":\"0\",\"picture_length\":\"0\",\"picture_name\":\"test\",\"retrain\":\"1\"}"
    jhead = "{\"Content-Length\":10,\"picture_length\":10,\"picture_name\":\"test\"}"
    msg = str(len(jhead))
    #msg = '12'
    if len(msg) < 12:
        fix = 12 - len(msg)
        for x in range(0, fix):
            msg = '0' + msg
            print(msg)
        # continue
    # msg = base64.b64encode(msg)  # 发送的是2进制码子？
    s.send(msg.encode('utf-8'))  # 向服务器发送消息
    # s.send("a0001fdg".encode())
    # s.send("abcdefdg".encode())
    s.send(jhead.encode())
    if (int)(msg) == 63:
        print('msg...length ok...')
        s.send("123456789".encode())
    # s.send(str.encode())
    data = s.recv(BUFFSIZE).decode()  # 接收服务器的消息

    print('Received:', data)
    time.sleep(1)
    # break
s.close()

#if __name__ == '__main__':
 #   print("oooooo")
