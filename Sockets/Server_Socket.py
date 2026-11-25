import socket

# This a the line that creates the server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This creates IP and Port Variable as one argument 
addressport = ("127.0.0.1", 9900)

# Creating the Bind
serversocket.bind(addressport)

# This is a test print to confirm the socket is created
print (serversocket)