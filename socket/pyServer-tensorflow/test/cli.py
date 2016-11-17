import socket, struct


def main(host):
    # Connect to server and get image size.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, 9999))
    except Exception as e:
        print str(e)
    with open('111.jpg', 'rb') as file:
        data = file.read()

    # Construct message with data size.
    size = struct.pack('!I', len(data))
    print size,type(size)
    message = size + data
    print message,type(message)
    client.sendall(message)
    msg = client.recv(1024)
    print msg
    client.close()

if __name__ == '__main__':
	main('127.0.0.1')
