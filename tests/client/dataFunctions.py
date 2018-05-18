import socket

# function to send both size of data and data
def sendData(sock, data):

    # set a header of 10 bytes with the size of data
    # this is to ensure no data is lost when sending
    dataSize = str(len(data))

    while len(dataSize) < 10:
        dataSize = "0" + dataSize

    data = dataSize + data
    dataSent = 0

    # check if all data is sent
    while dataSent != len(data):
        dataSent += sock.send(data[dataSent])



# function to recieve both size of data and data
def recvAll(sock, dataSize):
    recvBuffer = ""
    tempBuffer = ""

    # check if all data is received
    while len(recvBuffer) < dataSize:
        tempBuffer = sock.recv(dataSize)

        # if reciever/sender closes sock
        if not tempBuffer:
            break

        recvBuffer += tempBuffer

    return recvBuffer
        


# reads the header and returns the data with no loss
def recv(sock):
    data = ""
    fileSize = 0
    fileSizeBuffer = ""
    
    #create a buffer for the header size
    fileSizeBuffer = recvAll(sock, 10)

    try:
        fileSize = int(fileSizeBuffer)
        data = recvAll(sock, fileSize)

    except:
        pass
        
    return data

