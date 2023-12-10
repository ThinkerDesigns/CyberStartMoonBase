import socket

def debugMsg(msg):
    # Use this function if you need any debug messages
    with open("/tmp/userdebug.log", "a") as myfile:
        myfile.write(msg + "\n")

def main():
    # Define the server address
    server_address = ('localhost', 10000)

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the server address
        server_socket.bind(server_address)

        # Listen for incoming connections
        server_socket.listen()

        print(f"Server listening on {server_address}")

        # Accept connections from clients
        while True:
            client_socket, client_address = server_socket.accept()

            try:
                # Receive data from the client
                data = client_socket.recv(1024).decode()

                # Record the signal to /tmp/aliensignallog.txt
                with open("/tmp/aliensignallog.txt", "a") as signal_log:
                    signal_log.write(data + "\n")

                print(f"Received signal: {data}")

            except Exception as e:
                debugMsg(f"Error: {e}")

            finally:
                # Close the connection with the client
                client_socket.close()

if __name__ == "__main__":
    main()
