import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to {0}:{1}'.format(*server_address), file=log_buffer)
    sock.connect(server_address)

    received_message = b''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.send(msg.encode())

        # the server should be sending you back your message as a series
        # of 16-byte chunks. Accumulate the chunks you get to build the
        # entire reply from the server. Make sure that you have received
        # the entire message and then you can break the loop.
        chunk = b''
        while True:
            chunk = sock.recv(16)
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            received_message += chunk
            if len(chunk) < 16:
                break

    except Exception as e:
        print('caught exception {0}'.format(e), file=log_buffer)
        raise e

    finally:
        print('closing socket', file=log_buffer)
        sock.close()
        return received_message.decode()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
