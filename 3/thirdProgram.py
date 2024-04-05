import socket, sys, argparse

def Timeout(tot):
    try:
        #Create a new connection
        s = socket.create_connection(('www.google.com', 80), timeout=tot)
        print("\nConnection Successful")

        #Get timeout of connection.
        print(f'Timeout before setting: {s.gettimeout()}')

        #Set New Timeout value to 100
        s.settimeout(100)
        print(f'Timeout after setting new value: {s.gettimeout()} \n')
              
    except socket.error as e:
        print(f'Socket Error : {e}')
        sys.exit()

def usingArgparse():
    try:
        parser = argparse.ArgumentParser(description='Create arguments for host, port and filename.')
        
        # Adding command-line arguments
        parser.add_argument('--host', dest='host', required=True, help='Host address')
        parser.add_argument('--port', dest='port', required=True, type=int, help='Port number')
        parser.add_argument('--filename', dest='filename', required=True, help='File name')

        #Adds argument values to args namespace.
        args = parser.parse_args()

        #print argument values from args namespace.
        print(f'Host: {args.host}')
        print(f'Port: {args.port}')
        print(f'Filename: {args.filename}')

    except argparse.ArgumentError as e:
        print(f"Error parsing command-line arguments: {e}")
        sys.exit()

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

def sendRecieve():
    #Create Socket Object
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Socket Error: {e}')

    #Connect to a remote host.
    try:    
        s.connect(('www.google.com', 80))
    except socket.error as e:
        print(f'Socket Error: {e}')

    #Send a message to host.
    try:
        query = "One Piece"
        msg = "GET /search?q={query} HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print(f'Socket Error: {e}')

    #Recieve a message of specified size.
    try:    
        res = s.recv(2048)
        text_content = res.decode('ISO-8859-1')
        print(text_content)
    except socket.error as e:
        print(f'Socket Error: {e}')


if __name__ == '__main__':
    Timeout(24)
    usingArgparse()
    sendRecieve()