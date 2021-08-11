import socket
import sys
import os
from wakeonlan import send_magic_packet
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping -c 1', param, '1', host]

    return subprocess.call(command) == 0





if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)


# Create socket for server
sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program")


server_address = (ip, port)
send_data = ""



while (send_data != 'q'):
    send_data = input("1 - Check PC Status \n 2 - Open PC \n 3 - Shut down PC \n")
    sckt.sendto(send_data.encode('utf-8'), (ip, port))
    if(send_data == '1'):
        print("Pinging" + ip + '\n')
        isPcOn = ping(ip)

        if(isPcOn):
            print("PC status : ON\n")
        else:
            print("PC status : OFF\n")

    if(send_data == '2'):
        print("Waking PC\n")
        send_magic_packet("04:D9:F5:35:03:94")
        while(not(ping(ip))):
            print('.')


sckt.close()
#"Type some text to send or press q to exit=>"







    