#
# Send server ('localhost', 10000) GET_KEY to retrieve key,
# user needs to reverse and send back to server to get flag.
# It will change each execution so the
# user can not manually achieve this.
#
import socket

def get_reversed_key(original_key):
    # Reverse the key
    reversed_key = original_key[::-1]
    return reversed_key

# Set the server address and port
server_address = ('localhost', 10000)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect(server_address)

    # Send the command to get the key
    command = 'GET_KEY'
    client_socket.sendall(command.encode())

    # Receive and print the key from the server
    key = client_socket.recv(1024).decode()
    print("Key from server:", key)

    # Reverse the key
    reversed_key = get_reversed_key(key)
    print("Reversed key:", reversed_key)

    # Send the reversed key back to the server to get the flag
    client_socket.sendall(reversed_key.encode())

    # Receive and print the flag from the server
    flag = client_socket.recv(1024).decode()
    print("Flag from server:", flag)

finally:
    # Close the socket
    client_socket.close()
