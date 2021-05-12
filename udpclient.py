import socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = input ('Input Lower case message:')
data = message.encode('ascii')

# Send Data
s.sendto(data,('127.0.0.1',3000))
print('OS Provided IP and Port {}'.format(s.getsockname()))

# Recieve Data
data, address = s.recvfrom(MAX_SIZE_BYTES)
response = data.decode('ascii')
print('Server {} responded with {!r}'.format(address,response))
