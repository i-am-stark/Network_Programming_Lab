import socket

def Unblock():
    #Create a TCP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to host, default blocking state is True. The connection should be successful.
    try:
        print("\nDefault blocking state is : True. Trying to connect.")
        s.connect(('www.google.com', 80))
        print("Connection Successful")
        s.close()

    except socket.error as e:
        print(f"Error while connecting: {e}")

    #Create a TCP Socket and set blocking state to False. The connection should be unsuccessful.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
     
    try:
        print("\nThe blocking state is set to : False. Trying to connect")
        s.connect(('www.google.com', 80))
    except BlockingIOError as e:
        print(f"Error while connecting: {e}")
   

def Block():
    #Create a TCP Socket.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Set blocking state to True.
    s.setblocking(True)

    #Connect to host, since blocking state is true, it should be successful.
    try:
        print("\nThe blocking state is set to : True. Trying to connect.")
        s.connect(('www.google.com', 80))
        print("Connection Successful")
        s.close()

    except socket.error as e:
        print(f"Error while connecting: {e}")


def changeBufferSize(buff):
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the current buffer size
    rcv_buff = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    snd_buff = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)

    print(f"\nCurrent receive buffer size: {rcv_buff} bytes")
    print(f"Current send buffer size: {snd_buff} bytes")

    # Modify the buffer size
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, buff)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, buff)

    # Get the modified buffer size
    rcv_buff = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    snd_buff = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)

    print(f"\nModified receive buffer size: {rcv_buff} bytes")
    print(f"Modified send buffer size: {snd_buff} bytes")

    s.close()


def main():
    buff = int(input())
    Unblock()
    Block()
    changeBufferSize(buff)

if __name__ == "__main__":
    main()