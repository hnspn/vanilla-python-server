from socket import socket, gethostname

server = socket()

server.bind(('0.0.0.0', 5000))
server.listen()

while True:
    print('waiting for connections')

    clientsocket, address = server.accept()
    print(f'New connection from {address}')

    data = ' '
    while data:
        print('waiting for messages from', address)
        data = clientsocket.recv(1024)
        print('client message:', data)
