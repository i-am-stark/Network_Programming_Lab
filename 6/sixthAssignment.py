import socket, sys

def start_server(host, port):
    try:
        # Create a TCP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Enable SO_REUSEADDR option
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the specified host and port
        server_socket.bind((host, port))

        # Start listening for incoming connections
        server_socket.listen(2)

        print(f"Server listening on {host}:{port}")

        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()

            # Handle the client connection
            print(f"Connection established from {client_address}")

            # Close the client socket 
            client_socket.close()
            
        
    except KeyboardInterrupt:
            print("Keyboard interrupt received. Exiting...")
            sys.exit(0)

    except socket.error as e:
        print(f"Socket error: {e}")
   
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Localhost
    PORT = 106  # Port to listen on

    start_server(HOST, PORT)
