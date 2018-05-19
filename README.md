# Simplified-FTP-Server

## Programming Language:
PYTHON 2.7

## How to execute the program:

### To initiate the FTP Server: 
python serv.py <PORT NUMBER>

### To run the FTP client: 
python cli.py <server machine> <server port>


#### Upon connecting to the server, the client prints out ftp>. Here the user can enter the following commands:

1. ftp> get <file name> (downloads ﬁle <ﬁle name> from the server) 
2. ftp> put <filename> (uploads ﬁle <ﬁle name> to the server)
3. ftp> ls (lists ﬁles on the server) 
4. ftp> lls (lists ﬁles on the client) 
5. ftp> quit (disconnects from the server and exits)

