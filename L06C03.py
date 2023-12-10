#
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#
import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 10000)
client_socket.connect(server_address)

# Send command to list files in /tmp
command = "ls /tmp"
client_socket.sendall(command.encode())

# Receive response
data = client_socket.recv(1024).decode()

# Print the received data
print(data)

# Close the socket
client_socket.close()
