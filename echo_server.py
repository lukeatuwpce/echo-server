import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)
            sock.listen()
            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                while True:
                    data = conn.recv(16)
                    print('received "{0}"'.format(data.decode('utf8')))

                    if not data:
                        print('EOM; breaking')
                        break

                    conn.send(data)
                    print('sent "{0}"'.format(data.decode('utf8')))

            finally:
                print('echo complete, closing connection', file=log_buffer)
                conn.close()

    except KeyboardInterrupt:
        print('quitting echo server', file=log_buffer)
        sock.close()


if __name__ == '__main__':
    server()
    sys.exit(0)
