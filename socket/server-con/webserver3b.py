#########################################################################
# Iterative server - webserver3b.py                                     #
#                                                                       #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X      #
#                                                                       #
# - Server sleeps for 60 seconds after sending a response to a client   #
#########################################################################
import socket
import time
import os
import sys # fileno

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World22!
"""
    client_connection.sendall(http_response)
    time.sleep(10)  # sleep and block the process for 60 seconds

a = 0
def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print("backlog {backlog}...".format(backlog=REQUEST_QUEUE_SIZE))
    print('Serving HTTP on port {port} :{fileno}...'.format(port=PORT, fileno=listen_socket.fileno()))

    while True:
        client_connection, client_address = listen_socket.accept()
        global a
        a = a + 1
        print("a...is: %d" % a)

        handle_request(client_connection)

        if a > 3:
            print("go out ....%s" % time.ctime())
            exit();
        client_connection.close()

if __name__ == '__main__':
    pid = os.getpid()
    print("pid is:%d\n" % pid )
    serve_forever()