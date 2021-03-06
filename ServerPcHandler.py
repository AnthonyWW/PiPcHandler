import socket
import sys
import os

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
sckt.bind(server_address)

while True:
    print("####### Server is listening #######")
    data, address = sckt.recvfrom(4096)
    dataString = data.decode('utf-8')
    print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
    
    if(dataString == "shutdown"):
        os.system("shutdown /s /t 1")
        sckt.close()
        


