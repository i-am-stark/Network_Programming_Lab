import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address
server_address = ('localhost', 106)

# Bind the server to the address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening on port 106...")

# Dictionary to keep track of client connections
client_connections = {}

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()

    try:
        # Receive the data in small chunks and parse HTTP request
        data = connection.recv(1024).decode()
        print("Received HTTP request:")
        print(data) 

        # Extract client IP address
        client_ip = client_address[0]

        # Update client connections count
        if client_ip in client_connections:
            client_connections[client_ip] += 1
        else:
            client_connections[client_ip] = 1

        # Construct HTTP response
        response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
        response += f"<html><body>"
        response += f"<h1>Client IP: {client_ip}</h1>"
        response += f"<p>Number of times connected: {client_connections[client_ip]}</p>"
        response += f"</body></html>"

        # Send the HTTP response back to the client
        connection.sendall(response.encode())

    finally:
        # Clean up the connection
        connection.close()
