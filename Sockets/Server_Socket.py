import socket

# This a the line that creates the server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This is a test print to confirm the socket is created
print (serversocket)