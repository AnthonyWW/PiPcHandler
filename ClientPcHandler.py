import socket
import sys
from wakeonlan import send_magic_packet
import PcHandlerCommon as ph

SHUTDOWN = "shutdown"


if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)


# Create socket for server
sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program\n")


server_address = (ip, port)
send_data = ""

while (send_data != 'q'):
    send_data = input(" 1 - Check PC Status \n 2 - Open PC \n 3 - Shut down PC \n")
    sckt.sendto(send_data.encode('utf-8'), (ip, port))

    if(send_data == '1'):
        print("Pinging " + ip + '\n')
        print("\n")

        if(ph.ping(ip)):
            print("\nPC status : ON\n")
        else:
            print("\nPC status : OFF\n")
        
        send_data = ""

    if(send_data == '2'):
        print("Waking PC\n")
        send_magic_packet("04:D9:F5:35:03:94")

        while(not(ph.ping(ip))):
            print('.')

        print('\n')

    if(send_data == '3'):
        sckt.sendto(bytes(SHUTDOWN, "utf-8", (ip, port)))
        
        send_data = ""
    
sckt.close()
#"Type some text to send or press q to exit=>"



