import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('OS Provided IP and Port {}'.format(s.getsockname()))
