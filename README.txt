Simplified-FTP-Server

Names & Email-Addresses:

1. Imran Gosla      igosla0@csu.fullerton.edu
2. Joshua Najera    joshuanajera@csu.fullerton.edu
3. Kevin Pham       kpham163@csu.fullerton.edu
4. Luke Higgott     luke.higgott@csu.fullerton.edu
5. Timothy Nguyen   timnguyen@csu.fullerton.edu

Programming Language:
PYTHON 2.7

How to execute our program:

To initiate the FTP Server: 
    python serv.py <PORT NUMBER>

To run the FTP client: 
    python cli.py <server machine> <server port>


    Upon connecting to the server, the client prints out ftp>. Here the user can enter the following commands:

    ftp> get <file name> (downloads ﬁle <ﬁle name> from the server) 
    ftp> put <filename> (uploads ﬁle <ﬁle name> to the server)
    ftp> ls (lists ﬁles on the server) 
    ftp> lls (lists ﬁles on the client) 
    ftp> quit (disconnects from the server and exits)


Extra Credit:
    Not implemented