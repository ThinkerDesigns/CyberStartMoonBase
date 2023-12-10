import socket

def communicate_with_alien_server():
    # Define the server address
    server_address = ('localhost', 10000)

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the alien server
        s.connect(server_address)

        # Values to send
        values_to_send = ["USER", "aliensignal", "PASS", "unlockserver", "SEND", "moonbase", "END"]

        # Send and receive data for each value
        for value in values_to_send:
            # Send the value to the server
            s.sendall(value.encode())

            # Receive the response from the server
            data = s.recv(1024).decode()
            print(f"Sent: {value}, Received: {data}")

# Call the function to start communication
communicate_with_alien_server()
