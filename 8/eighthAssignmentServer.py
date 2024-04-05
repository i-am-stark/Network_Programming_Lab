import socket
import argparse

# Create a UDP Socket and bind it to a port.
def create_server_socket(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('127.0.0.1', port))
        print("UDP Socket successfully created and listening on port:", port)
        return server_socket
    except socket.error as e:
        print(f"Socket error: {e}")
        return None


# Recieve data form client and echo them back.
def receive_and_echo(server_socket):
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")
        server_socket.sendto(data, addr)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="UDP Server")
    parser.add_argument("--port", type=int, default=106, help="Port number")
    args = parser.parse_args()

    # Create server socket
    server_socket = create_server_socket(args.port)
    if server_socket:
        receive_and_echo(server_socket)

if __name__ == "__main__":
    main()
