import socket
import sys
import ipaddress as ipa

if len(sys.argv) == 4:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
    operationMode = sys.argv[3]
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)


# Create socket for server
sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program")


server_address = (ip, port)


# Let's send data through UDP protocol
while True:
    if(operationMode == "client"):
        send_data = input("Type some text to send =>");
        sckt.sendto(send_data.encode('utf-8'), (ip, port))
        print("\n\n 1. Client Sent : ", send_data, "\n\n")
        #data, address = socket.recvfrom(4096)
        #print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
    elif(operationMode == "server"):
        sckt.bind(server_address)
        print("####### Server is listening #######")
        data, address = sckt.recvfrom(4096)
        print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
        send_data = input("Type some text to send => ")
        socket.sendto(send_data.encode('utf-8'), address)
        print("\n\n 1. Server sent : ", send_data,"\n\n")

sckt.close()

# import socket
# import sys

# if len(sys.argv) == 3:
#     # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
#     ip = sys.argv[1]
#     port = int(sys.argv[2])
# else:
#     print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
#     exit(1)

# # Create socket for server
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# print("Do Ctrl+c to exit the program !!")

# # Let's send data through UDP protocol
# while True:
#     send_data = input("Type some text to send =>");
#     s.sendto(send_data.encode('utf-8'), (ip, port))
#     print("\n\n 1. Client Sent : ", send_data, "\n\n")
#     data, address = s.recvfrom(4096)
#     print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
# # close the socket
# s.close()