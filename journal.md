# journal

## problems encountered

- socket.bind((hostname, address)). the hostname can be 
  - 'localhost' : allows connections only from the same machine through the loopback interface
  - gethostname(): allow connections only from machines on the same network. no loopback interface
  - '0.0.0.0': allow connections from both
- socket.send() requires bytes. just converts string like this b'hello'
- socket.recv(n):
  - you call it on the client connection
  - blocks the process until there is data to be read or the connection is closed
  - it can be used to tell if the connction has terminated (if it returns nothing)
- I may have underestimated the complexity of an HTTP server. I think I will start with a simple chat server
- socket.accept() is blocking
  - I should dispatch a new thread for each new connections
  - or restructure the app to use async methods
