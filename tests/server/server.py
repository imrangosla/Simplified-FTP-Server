import socket
import commands
import argparse
import sys
import os
from dataFunctions import sendData, recvAll, recv


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
	print '{}{}{}'.format("User with IP: ", addr, " connected")


	# While connection is still established
	# Listen for commands
	try:
		while connection:
			print 'Waiting for command...'
			cmd = connection.recv(1024)
			if cmd:
				print 'command received: <{}>'.format(cmd)
				cmd_list = cmd.split()

				# Client sent too many args
				if len(cmd_list) > 3:
					connection.send('Invalid command syntax :(')

				if len(cmd_list) == 2:
					if cmd_list[0] == 'get':
						print "get"
					elif cmd_list[0] == 'put':
						print "put"
					
				if len(cmd_list) == 1:
					if cmd_list[0] == 'ls':
						print "ls"

	except IndexError:
		print 'Client dropped.'

	finally:
		connection.close()