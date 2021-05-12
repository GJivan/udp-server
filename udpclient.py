import socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram
HOST_NAME='127.0.0.1'
PORT=3000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = input ('Input Lower case message:')

s.connect((HOST_NAME,PORT))
data = message.encode('ascii')

# Send Data
s.send(data)
print('OS Provided IP and Port {}'.format(s.getsockname()))

# Recieve Data
data = s.recv(MAX_SIZE_BYTES)
response = data.decode('ascii')
print('Server responded with {!r}'.format(response))
