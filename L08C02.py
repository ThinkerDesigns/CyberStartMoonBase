#
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send 'GET_KEY' to download a string.
# The string is compressed with a common algorithm found in many
# websites. Decompress the string and print it to get the flag.
#
import socket
import zlib
import gzip
import bz2

# Set the server address and port
server_address = ('localhost', 10000)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect(server_address)

    # Send the 'GET_KEY' request to retrieve the compressed string
    client_socket.sendall('GET_KEY'.encode())

    # Receive the compressed string from the server
    compressed_data = client_socket.recv(1024)

    try:
        # Attempt zlib decompression
        decompressed_data = zlib.decompress(compressed_data)
    except zlib.error:
        try:
            # Attempt gzip decompression
            decompressed_data = gzip.decompress(compressed_data)
        except gzip.error:
            try:
                # Attempt bz2 decompression
                decompressed_data = bz2.decompress(compressed_data)
            except bz2.error:
                print("Error: Unable to decompress the data.")
                decompressed_data = None

    # Print the decompressed string (flag) if successful
    if decompressed_data is not None:
        print("Decompressed String (Flag):", decompressed_data.decode('utf-8'))

finally:
    # Close the socket
    client_socket.close()
