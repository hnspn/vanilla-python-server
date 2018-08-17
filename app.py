from socket import socket, gethostname

server = socket()

server.bind(('0.0.0.0', 5000))
server.listen()

while True:
    client_socket, address = server.accept()
    print(f'New connection from {address}')
    help(client_socket)
    client_socket.send(b'Thanks')
    client_socket.close()
