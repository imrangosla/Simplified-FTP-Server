import socket
import os

# The port on which to listen
listenPort = 1234

# Create a welcome socket. 
welcomeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
welcomeSock.bind(('', listenPort))

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
				filename = cmd_list[1]
				print 'trying to put a file named {}'.format(filename)
				ephemeral_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				ephemeral_port.bind(('', 0))
				print 'new ephemeral port created on {}'.format(ephemeral_port.getsockname()[1])

    		if cmd_list[0] == 'ls':
				pass
    	        # run ls on server and return output to client
	except IndexError:
		print 'I think our client dropped.'
	finally:
		connection.close()