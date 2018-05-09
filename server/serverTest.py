import socket

# The port on which to listen
listenPort = 1234

# Create a welcome socket. 
welcomeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
welcomeSock.bind(('', listenPort))

# Start listening on the socket
welcomeSock.listen(1)

def recvAll(sock, numBytes):

	# The buffer
	recvBuff = ""
	
	# The temporary buffer
	tmpBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff
	
	return recvBuff


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
			cmd = connection.recv(1024)
			print 'command received: <{}>'.format(cmd)
			cmd_list = cmd.split()

			if len(cmd_list) > 2:
				connection.send('Invalid command syntax :(')
				
			if cmd_list[0] == 'get':
				print 'hello asshole this is an indented block'
     	        # send file cmd_list[1] to client

     		if cmd_list[0] == 'put':
				filename = cmd_list[1]
				print 'trying to put a file named {}'.format(filename)
				ephemeral_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				ephemeral_port.bind((''), 0)
				print 'new ephemeral port created on {}'.format(ephemeral_port.getsockname()[1])

    		if cmd_list[0] == 'ls':
				pass
    	        # run ls on server and return output to client
	finally:
		connection.close()