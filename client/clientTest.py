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
print "Connecting..."
connSock.connect((serverAddr, serverPort))

socket.setdefaulttimeout(3)


active = True
while active:

    # set format for program
    cmd = raw_input("\nftp> ")
    input_list = cmd.split()
    print len(input_list)
    if len(input_list) == 2:

        if input_list[0] == 'get':
            # send 'get' to the server
            print "Sent Get"

            # Set up listening socket
            inSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            inSock.bind(('', 0))
            # Let server know what you want
            connSock.sendall('get %s %d' % (input_list[1], inSock.getsockname()[1]))
            # Listen for server's connection
            inSock.listen(1)
            connection, _ = inSock.accept()
            # Create a space to receive data
            rcvd_data = connection.makefile()
            data = rcvd_data.read()
            # Cleaning connections
            connection.close()
            inSock.close()
            rcvd_data.close()
            # Make surethe file was there before writing to disk
            if data:
                outFile = open(input_list[1], 'w')
                outFile.write(data)
                outFile.close()
            else:
                print 'File doesn\'t exist'

        elif input_list[0] == 'put':
            # send 'put' to the server
            connSock.sendall('put %s' % input_list[1])
            print "Send Put"
        
        else:
            print "Invalid command"
        
    elif input_list[0] == 'quit':
        active = False
        exit()

    else:
        # raise SyntaxError('Invalid Command')
        print "Invalid command"

