import socket
import os
import sys
import commands

# Server address
serverAddr = "localhost"

# Server port
serverPort = 1234

# Create a TCP socket
connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connSock.connect((serverAddr, serverPort))

active = True
while active:

    # set format for program
    cmd = raw_input("ftp> ")
    input_list = cmd.split()
    
    if len(input_list) == 2:

        if input_list[0] == 'get':
            # send 'get' to the server
            print "Send Get"
            connSock.sendall('get %s' % input_list[1])

        elif input_list[0] == 'put':
            # send 'put' to the server
            print "Send Put"
        
    elif input_list[0] == 'quit':
        active = False
        exit()

    else:
        raise SyntaxError('Invalid Command')

