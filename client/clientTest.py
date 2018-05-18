import socket
import os
import sys
import commands
import argparse


# Use arguments parser to setup args
parser = argparse.ArgumentParser(description="Simplified-FTP-Client")
parser.add_argument("serverAddress", help="Server Address")
parser.add_argument("serverPort",  help="Port #")

args = parser.parse_args()
serverAddr = args.serverAddress
serverPort = args.serverPort

# port validation
if serverPort.isdigit():
    serverPort = int(serverPort)
else:
    print("ERROR: {} is not a valid port \n[Defaulting to port 1234]".format(serverPort))
    serverPort = 1234

# Create a TCP socket
connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
print "Connecting..."

connSock.connect((serverAddr, serverPort))    
socket.setdefaulttimeout(3)
print '{}{}'.format('Conncted on port: ', serverPort)
print '{}{}'.format('Conncted on Address: ', serverAddr)

active = True

while active:

    # set format for program
    cmd = raw_input("\nftp> ")

    # split input into array based off of space delimiter
    input_list = cmd.split()
    
    # print length of input for debugging purposes
    # print len(input_list)

    # if input list exactly two strings (i.e. get image.png, put image.png)
    if len(input_list) == 2:
        # define file name
        fileName = input_list[1]

        if input_list[0] == 'get':
            # Set up listening socket
            inSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            inSock.bind(('', 0))

            # Let server know what you want
            connSock.sendall('get %s %d' % (fileName, inSock.getsockname()[1]))

            # Listen for server's connection
            inSock.listen(1)
            connection, _ = inSock.accept()

            # Create a space to receive data
            print "Contacting server..."
            rcvd_data = connection.makefile()
            data = rcvd_data.read()
            print "*Received Data*"

            # Cleaning connections
            print "[Closing data connections]"
            connection.close()
            inSock.close()
            rcvd_data.close()
            print "SUCCESS"
            
            # Make sure the file was there before writing to disk
            if data:
                outFile = open(fileName, 'w')
                outFile.write(data)
                outFile.close()
            else:
                print 'File doesn\'t exist'

        # Want to put file onto server
        elif input_list[0] == 'put':
            # create a temporary socket to transfer port number and data
            tempSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tempSock.bind(('', 0))

            # send put and port number to server
            connSock.sendall('put %s %d' % (fileName, tempSock.getsockname()[1]))

            # Listen for server's connection
            tempSock.listen(1)
            connection, _ = tempSock.accept()

            # Check if file exists first
            if os.path.isfile(fileName):
                data = open(fileName, 'r')
                data = data.read()
                if data:
                    print "data exists"
                tempSock.sendall(data)
                print 'Data sent\n'
            else:
                print 'File doesn\'t exist'
                tempSock.sendall("")

            # Cleaning connections
            tempSock.close()

        # if first word in list that is more than two strings is not put or get
        else:
            print ""

    if len(input_list) == 1:

        if input_list[0] == 'lls':
            print "Files on client are:"
            for line in commands.getstatusoutput('ls -l'):
                print line

        elif input_list[0] == 'ls':
            print "Files on server are: \n"

             # Set up listening socket
            inSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            inSock.bind(('', 0))

            # Let server know we want the ls command run on it
            connSock.sendall('ls')

            # Listen for server's connection
            inSock.listen(1)
            connection, _ = inSock.accept()

            # Create a space to receive data
            rcvd_data = connection.makefile()
            data = rcvd_data.read()

            #Print the ls command that was received from server
            print data

            # Cleaning connections
            connection.close()
            inSock.close()
            rcvd_data.close()

        elif input_list[0] == 'quit':
            active = False
            exit()
        
        else:
            print "ERROR: [Invalid command]"