import argparse, socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram



def server(port):
    pass
    # Your code goes here

def client(port):
    pass
    # Your code goes here

if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)
