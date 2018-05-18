import socket
import commands
import os
import argparse

# Use arguments parser to setup args
parser = argparse.ArgumentParser(description="Simplified-FTP-Server")
parser.add_argument("port",  help="Port #")

args = parser.parse_args()
listenPort = args.port


# port validation
if listenPort.isdigit():
    listenPort = int(listenPort)
else:
    print("ERROR: {} is not a valid port \n[Defaulting to port 1234]".format(listenPort))
    listenPort = 1234


# socket initiation
welcomeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcomeSock.bind(('', listenPort))
print "Socket started..."


# Start listening on the socket
welcomeSock.listen(1)


# Accept connections forever
while True:
	
	print "Waiting for connections..."
		
	# Accept connections
	connection, addr = welcomeSock.accept()
	
	print "User connected with IP and PORT: {}:{}".format(addr[0], addr[1])
	
	# While connection is still established
	# Listen for commands
	try:
		while connection:
			print 'waiting for command'
			cmd = connection.recv(1024)
			print 'command received: <{}>'.format(cmd)
			cmd_list = cmd.split()

			# Client sent too many args
			if len(cmd_list) > 3:
				connection.send('Invalid command syntax :(')
				
			# Client wants a file
			if cmd_list[0] == 'get':
				# Connect to client's socket
				dataSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				dataSock.connect((addr[0], int(cmd_list[2])))

				# Check if file exists first
				if os.path.isfile(cmd_list[1]):
					data = open(cmd_list[1], 'r')
					data = data.read()
					dataSock.sendall(data)
					print 'Data sent\n'
				else:
					print 'File doesn\'t exist'
					dataSock.sendall("")

				# Cleaning up
				dataSock.close()
				
			if cmd_list[0] == 'put':
				# Connect to client's socket
				dataSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				dataSock.connect((addr[0], int(cmd_list[2])))

				# Create a space to receive data
				print "Contacting server..."
				rcvd_data = connection.makefile()
				data = rcvd_data.read()
				print "*Received Data*"

				# Cleaning connections
				print "[Closing data connections]"
				dataSock.close()
				rcvd_data.close()
				
				# Make sure the file was there before writing to disk
				if data:
					outFile = open(cmd_list[1], 'w')
					outFile.write(data)
					outFile.close()
					print "SUCCESS"
				else:
					print 'File doesn\'t exist'



    		if cmd_list[0] == 'ls':
				# The LS command for server's files, saved to a string.
				sendingString = ""

				# print sendingString
				for i in commands.getstatusoutput('ls -l'):
					sendingString += str(i)

				# Connect to client's socket
				dataSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				dataSock.connect((addr[0], int(cmd_list[1])))

				# Send the string
				dataSock.sendall(sendingString)

				# Close socket
				dataSock.close()
			
			
	except IndexError:
		print 'I think our client dropped.'
	finally:
		connection.close()