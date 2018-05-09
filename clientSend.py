# *******************************************************************
# This file illustrates how to send a file using an
# application-level protocol where the first 10 bytes
# of the message from client to server contain the file
# size and the rest contain the file data.
# *******************************************************************
import socket
import os
import sys


# Command line checks 
if len(sys.argv) < 2:
	print "USAGE python " + sys.argv[0] + " <FILE NAME>" 

# Server address
serverAddr = "localhost"

# Server port
serverPort = 1234

# The name of the file
fileName = sys.argv[1]

# Open the file
fileObj = open(fileName, "r")

# Create a TCP socket
connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connSock.connect((serverAddr, serverPort))

# The number of bytes sent
numSent = 0

# The file data
fileData = None

''' Main loop '''
quit = False

while not quit:
    # sets format for program
    cmd = raw_input("ftp> ")

    # if there is a space in the input
    if ' ' in cmd:

        # convert input into an array
        input_array = cmd.split(' ')

        if input_array[0] == 'get':
            if input_array[1]:
                # get rid of the quit later, its for testing purposed right now
                quit = True

                continue
            else:
                print "INPUT ERROR: FILE NOT FOUND"
                
        elif input_array[0] == 'put':
            if input_array[1]:
                # get rid of the quit later, its for testing purposed right now
                quit = True
                
            else:
                print "INPUT ERROR: NO FILE PROVIDED"
        
        else:
            print "INPUT ERROR: CHECK YOUR COMMANDS"


    elif cmd == 'ls':
        print "this will list files on the server"

    elif cmd == 'lls':
        print "this will list files on the client"

    elif cmd == 'quit':
        quit = True

    else:
        print "ERROR"


        
    

# Keep sending until all is sent
''' Separate this loop to its own function for sending ''' 
while True:
    
    # Read 65536 bytes of data
    fileData = fileObj.read(65536)
    
    # Make sure we did not hit EOF
    if fileData:
        
            
        # Get the size of the data read
        # and convert it to string
        dataSizeStr = str(len(fileData))
        
        # Prepend 0's to the size string
        # until the size is 10 bytes
        while len(dataSizeStr) < 10:
            dataSizeStr = "0" + dataSizeStr
    
    
        # Prepend the size of the data to the
        # file data.
        fileData = dataSizeStr + fileData	
        
        # The number of bytes sent
        numSent = 0
        
        # Send the data!
        while len(fileData) > numSent:
            numSent += connSock.send(fileData[numSent:])
    
    # The file has been read. We are done
    else:
        break


print "Sent ", numSent, " bytes."
    
# Close the socket and the file
connSock.close()
fileObj.close()
	 


