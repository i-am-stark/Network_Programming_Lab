import socket, binascii
name = socket.gethostname()

def remote_ip():
    try:
        ip = socket.gethostbyname(name)
        print(f'The IP Address of remote machine is: {ip} \n')
    except:
        print('Some error occurred, could not get host IP \n')

def format_conversion(): 
    ip = socket.gethostbyname(name)  
    byte_ip = socket.inet_aton(ip)
    hxIP = binascii.hexlify(byte_ip).decode('utf-8')
    print(f'Hexadecimal represenatation of host IP: {hxIP} \n')
    bin_IP = binascii.unhexlify(hxIP)
    print(f'Binary represenatation of host IP: {bin_IP} \n')

def service_name():
    for i in range(1,1001):
        try:    
            service_name = socket.getservbyport(i, 'tcp')
            print(f'\n {service_name}')
        except:
            print('', end='')

def main():
    remote_ip()
    format_conversion()
    service_name()

    
if __name__ == "__main__":
    main()

