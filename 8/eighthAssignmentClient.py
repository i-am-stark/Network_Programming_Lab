import socket
import argparse

# Create a client Socket.
def create_client_socket():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return client_socket
    except socket.error as e:
        print(f"Socket error: {e}")
        return None

# Send message to server and recieve the echoed message.
def send_and_receive(client_socket, server_address, server_port):
    message = input("Enter message to send:")
    client_socket.sendto(message.encode(), (server_address, server_port))
    response, addr = client_socket.recvfrom(4096) 
    print(f"Received echo from {addr}: {response.decode()}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="UDP Client")
    parser.add_argument("--server", type=str, default="127.0.0.1", help="Server IP address")
    parser.add_argument("--port", type=int, default=106, help="Port number")
    args = parser.parse_args()

    # Create client socket
    client_socket = create_client_socket()
    if client_socket:
        send_and_receive(client_socket, args.server, args.port)
        client_socket.close()

if __name__ == "__main__":
    main()
