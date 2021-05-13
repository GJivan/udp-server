import argparse, socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram
HOST_NAME='127.0.0.1'


def server(port):
    pass
    #Creating Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST_NAME,port))


    # Listen Forever
    while True:
        data, clientAddress = s.recvfrom(MAX_SIZE_BYTES) # Wait for Message

        message = data.decode ('ascii')
        print('Source: {} Message {!r}'.format(clientAddress, message))

        message = input ('Input Server message:')
        data = message.encode('ascii')


        s.sendto(data,clientAddress)

def client(port):
    pass
 
    # Connect to Server
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect((HOST_NAME,port))


    while True: 
        message = input ('Input Client message:')
        data = message.encode('ascii')

        # Send Data
        s.send(data)
        print('OS Provided IP and Port {}'.format(s.getsockname()))

        # Recieve Data
        data = s.recv(MAX_SIZE_BYTES)
        response = data.decode('ascii')
        print('Server responded with {!r}'.format(response))



if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)
