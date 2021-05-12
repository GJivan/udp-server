import socket

#Creating Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 3000
hostname = '127.0.0.1'

s.bind((hostname,port))
print(s) # Print Socket Object
print('Listening at {}'.format(s.getsockname())) # Print IP and Port of Socket

