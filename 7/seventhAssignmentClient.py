import socket

#Create Client Socket
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
    print("Socket successfully created")

except socket.error as e:
    print(f"Socket error: {e}")

server_address = '127.0.0.1'
server_port = 106

#Connect to server.
client_socket.connect((server_address, server_port)) 
client_socket.settimeout(1)

message_count = 0

# Recieve message from server.  
while True:
    message = input("Enter message to send:")
    client_socket.send(message.encode())
    received_echo = client_socket.recv(1024).decode()
    print(f"Recieved Echo: {received_echo}")
    
client_socket.close()
