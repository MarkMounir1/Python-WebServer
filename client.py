import socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8080
clientSocket.connect((host, port))
clientSocket.sendall("GET /index.html HTTP/1.1\r\n".encode())#sendall vs send
clientSocket.send("\r\n".encode())
while True:
    message = clientSocket.recv(1024).decode()
    if len(message) == 0:
        break
    print(message)
clientSocket.close()