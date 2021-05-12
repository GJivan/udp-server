import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = input ('Input Lower case message:')
data = message.encode('ascii')
s.sendto(data,('127.0.0.1',3000))
print('OS Provided IP and Port {}'.format(s.getsockname()))
