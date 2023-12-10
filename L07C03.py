#
# Setup server listening on ('localhost', 10000)
# receive data then send data back after XORing with the key
# attackthehumans
#
# If you get an address already in use error then try again in a few
# moments.
#

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\\n")
import socket

def xor_encrypt(data, key):
    # XOR each byte of the data with the corresponding byte of the key
    encrypted_data = bytes([a ^ b for a, b in zip(data, key.encode())])
    return encrypted_data

# Set the server address and port
server_address = ('localhost', 10000)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print('Server listening on {}:{}'.format(*server_address))

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()
    print('Connection from', client_address)

    try:
        # Receive data from the client
        data = connection.recv(1024)
        if not data:
            break

        # XOR the data with the key
        key = "attackthehumans"
        encrypted_data = xor_encrypt(data, key)

        # Send the encrypted data back to the client
        connection.sendall(encrypted_data)
        print('Data sent back to the client:', encrypted_data)

    finally:
        # Clean up the connection
        connection.close()
