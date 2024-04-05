import socket
name = socket.gethostname()
print(f"The name of this computer is : {name}")
ip = socket.gethostbyname(name)
print(f"The IPV4 address of this computer is: {ip}")