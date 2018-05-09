# Simplified-FTP-Server

REQUIREMENTS

Client initially connects:

1. Connects via port specified on command line

2. Server prints out IP address + Port of client connected

3. Server prints SUCCESS/FAILURE based on command/request
	- for every command except lls

4. At end of transfer, connection is closed



Client wants to transfer data:

1. Server generates ephemeral port

2. Sends ephemeral port to client
	- this port is used for data connection

3. Server waits for client to connect on ephemeral port

4. Connection is used for data upload/download to/from server

5. Connection closes when data transfer is complete


NEED TO MAKE:
1. GET Command
	- get <file name> 
	- downloads file from server
2. PUT command
	- put <file name>
	- uploads file to server
3. LS Command
	- lists files on the server
4. LLS command
	- lists files on the client
5. QUIT Command
	- disconnects from server and exits