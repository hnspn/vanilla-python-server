from socket import socket, gethostname
from data import getrandomname
from threading import Thread


server = socket()

server.bind(('0.0.0.0', 5000))
server.listen()


def manageclient(clientsocket, username):
    while True:
        try:
            message = clientsocket.recv(1024)
            if message:
                for client in clients:
                    if client is not clientsocket:
                        client.send(username.encode() + b': ' + message)
                print(f'{username}: ', message)
            else:
                raise error(f'{username} has disconnected')
        except Exception as e:
            print(e)
            print('an error has occured\nthe connection will be closed')
            clientsocket.close()
            return False

clients = []
while True:
    print('waiting for connections')

    clientsocket, address = server.accept()
    clients.append(clientsocket)
    username = getrandomname()
    print(f'New connection from {username} at {address}')
    clientsocket.send(b'Welcome ' + username.encode() + b'\n')

    client_thread = Thread(target=manageclient, args=(clientsocket, username))
    client_thread.start()
