import struct, socket, time, ntplib

def getNtpTime(NTP_SERVER):
    try:
        #Create an instance of NTPClient.
        client = ntplib.NTPClient()

        # Make a request to the NTP server
        response = client.request(NTP_SERVER)
        ntpTime = time.ctime(response.tx_time)
        print(f'\nThe Time recieved through NTP: {ntpTime}')

    except ntplib.NTPException as e:
        print(f"NTPException: {e}")


def getSntpTime(NTP_SERVER, data, TIME1970):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(f'Socket Error: {e} ')
    
    try:
        s.sendto(data, (NTP_SERVER, 123))
    except socket.error as e:
        print(f'Socket Error: {e} ')

    try:
        res, addr = s.recvfrom(1024)
    except socket.error as e:
        print(f'Socket Error: {e} ')

    if data:
        #unpack the binary packed data.
        tm = struct.unpack('!12I', res)[10]

        #use epoch time to get current time.
        tm -= TIME1970

        #print time in readable format.
        sntpTime = time.ctime(tm)
        print(f'The Time recieved through SNTP: {sntpTime}')

def printBirthDate(dob):
    dob = time.ctime(dob)
    print(f'My birth date: {dob}\n')


if __name__ == '__main__':
    NTP_SERVER = "europe.pool.ntp.org"
    TIME1970 = 2208988800
    data = b'\x1b' + 47 * b'\0'

    #get epoch value of your birthdate from epochconverter.com
    dob = 933966900

    getNtpTime(NTP_SERVER)
    getSntpTime(NTP_SERVER, data, TIME1970)
    printBirthDate(dob)