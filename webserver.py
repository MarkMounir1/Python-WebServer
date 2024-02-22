from socket import *

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare server socket
serverPort = 8080
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    # Wait for a connection from a client
    connectionSocket, addr = serverSocket.accept()

    try:
        # Receive the HTTP request message from the client
        message = connectionSocket.recv(1024)

        # Extract the filename from the message
        filename = message.split()[1]

        # Open the requested file
        f = open(filename[1:])

        # Read the contents of the file
        outputdata = f.read()

        # Send the HTTP response message to the client
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n')
        connectionSocket.send(b'Content-Type: text/html\r\n')
        connectionSocket.send(b'\r\n')

        # Send the contents of the file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        # Close the client socket
        connectionSocket.close()

    # Handle file not found error
    except IOError:
        # Send a 404 Not Found HTTP response message to the client
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n')
        connectionSocket.send(b'Content-Type: text/html\r\n')
        connectionSocket.send(b'\r\n')
        connectionSocket.send(b'404 Not Found')

        # Close the client socket
        connectionSocket.close()