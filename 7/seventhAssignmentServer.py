import socket
import threading

# Function to handle each client connection
def handle_client(client_socket, address):
    print('Connection established with', address)
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Message from client {address}: {message}")
            client_socket.send(message.encode())
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        client_socket.close()
        print(f"Connection closed with {address}")

# Function to start the server
def start_server(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('127.0.0.1', port))
        server_socket.listen(5)
        print("Server started and listening on port:", port)
        
        while True:
            client_socket, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()
    except Exception as e:
        print(f"Error starting server: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server(106)
