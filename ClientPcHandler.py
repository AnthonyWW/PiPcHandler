import socket
import sys
from wakeonlan import send_magic_packet
import PcHandlerCommon as ph
from enum import Enum



SHUTDOWN = "shutdown"
CLOSE_COMMAND = 'q'


ip, port = ph.parse_config_file("config.txt")

if(ip == "" or port == 0):
    print("Invalid config file")
    exit(1)


# Create socket for server
sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Press Ctrl+c to exit the program\n")


server_address = (ip, port)
inputChoice = ""

while (inputChoice != 'q'):
    inputChoice = input(" 1 - Check PC Status \n 2 - Open PC \n 3 - Shut down PC \n")
    sckt.sendto(inputChoice.encode('utf-8'), (ip, port))

    if(inputChoice == ph.Choice.CHECK_PC_STATUS):
        print("Pinging " + ip + '\n')
        print("\n")

        if(ph.ping(ip)):
            print("\nPC status : ON\n")
        else:
            print("\nPC status : OFF\n")
        
        inputChoice = ""

    if(inputChoice == ph.Choice.OPEN_PC):
        print("Waking PC\n")
        send_magic_packet("04:D9:F5:35:03:94")

        while(not(ph.ping(ip))):
            print('.')

        print('\n')

    if(inputChoice == ph.Choice.CLOSE_PC):
        sckt.sendto(SHUTDOWN.encode("utf-8"), (ip, port))
        
        inputChoice = ""
    
sckt.close()
#"Type some text to send or press q to exit=>"



