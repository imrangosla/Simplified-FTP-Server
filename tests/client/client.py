import os
import sys
import commands
import argparse
import socket
from dataFunctions import sendData, recvAll, recv


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


# socket initiation
connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connSock.bind(('', serverPort))
print "Establishing socket..."

connSock.connect((serverAddr,serverPort))
print "Connecting to server..."
socket.setdefaulttimeout(3)

print '{}{}'.format('Conncted on port: ', serverPort)
print '{}{}'.format('Conncted on Address: ', serverAddr)
active = True



while active:
    # set format for program
    cmd = raw_input("\nftp> ")

    # split input into array based off of space delimiter
    input_list = cmd.split()

    # if input list exactly two strings (i.e. get image.png, put image.png)
    if len(input_list) == 2:

        # define file name
        fileName = input_list[2]

        if input_list[0] == 'get':
            print "send get"

        elif input_list[0] == 'put':
            # send 'put' and fileName to the server
            sendData(connSock, input_list)
            tempPort = int(recv(connSock))
            try:
                dataSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dataSock.connect((serverAddr, tempPort))
                sendData(dataSock, fileName)

                print "Uploading File to Server..."
                uploading = True

                while uploading:
                    try:
                        file = open(filename, "r")
                    except:
                        print "ERROR: [File can't be opened]"
                    try:
                        numBytes = 0
                        byte = file.read(1)
                        while byte != ""
                        
            except expression as identifier:
                pass
        
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

        elif input_list[0] == 'quit':
            active = False
            exit()
        
        else:
            print "ERROR: [Invalid command]"


