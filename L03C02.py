from time import sleep

import socket


# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('127.0.0.1', 9990))

# Send "Knock, knock" to the server
client_socket.send("Knock, knock".encode())

# Receive the response from the server
data = client_socket.recv(1024).decode()

# Print the response
print(f"Server response: {data}")

# Close the socket
client_socket.close()
sleep(0.05)
