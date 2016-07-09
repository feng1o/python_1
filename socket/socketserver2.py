
import server1


class MyTCPHandler(SocketServer.BaseRequestHandler):
    # 继承BaseRequestHandler基类，然后必须重写handle方法，并且在handle方法里实现与客户端的所有交互

    def handle(self):

        while True:
            data = self.request.recv(1024)  # 接收1024字节数据
            if not data:
                break
            self.request.sendall(data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 50007

    # 把刚才写的类当作一个参数传给ThreadingTCPServer这个类，下面的代码就创建了一个多线程socket server
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    # 启动这个server,这个server会一直运行，除非按ctrl-C停止
    server.serve_forever()
