

import socket

clientSocket = socket.socket();
clientSocket.connect(('localhost', 8080))
while True:
    clientSocket.send(input().encode())
    respuesta = clientSocket.recv(1024).decode()
    print(respuesta)

clientSocket.close()