# _*_ coding:utf-8 _*_
# socket server 1
"""
from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer(('127.0.0.1', 6666), EchoHandler)
    serv.serve_forever()"""

from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-like object for writing
            self.wfile.write(line)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    TCPServer.allow_resuse_address = True
    # serv.socket.setsockopt(socket.SOL_SOKCET,socket.SO_REUSEADDR, True);
    serv.serve_forever()