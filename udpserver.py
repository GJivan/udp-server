import socket

MAX_SIZE_BYTES = 65535 # Max Size of UDP Datagram

#Creating Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 3000
hostname = '127.0.0.1'

s.bind((hostname,port))
print(s) # Print Socket Object
print('Listening at {}'.format(s.getsockname())) # Print IP and Port of Socket

# Listen Forever
while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES) # Wait for Message
    
    message = data.decode ('ascii')
    upperCaseMessage = message.upper()
    
    print('Source: {} Message {!r}'.format(clientAddress, message))
    
    data =upperCaseMessage.encode('ascii')
    s.sendto(data,clientAddress)

