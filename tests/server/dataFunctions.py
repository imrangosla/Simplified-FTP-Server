import socket

# function to send both size of data and data
def sendData(socket, data):

    # set a header of 10 bytes with the size of data
    # this is to ensure no data is lost when sending
    dataSize = str(len(data))

    while len(dataSize) < 10:
        dataSize = "0" + dataSize

    data = dataSize + data
    dataSent = 0

    # check if all data is sent
    while dataSent != len(data):
        dataSent += socket.send(data[dataSent])



# function to recieve both size of data and data
def recvAll(socket, dataSize):
    recvBuffer = ""
    tempBuffer = ""

    # check if all data is received
    while len(recvBuffer) < dataSize:
        tempBuffer = socket.recv(dataSize)

        # if reciever/sender closes socket
        if not tempBuffer:
            break

        recvBuffer += tempBuffer

    return recvBuffer
        


# reads the header and returns the data with no loss
def recv(socket):
    data = ""
    fileSize = 0
    fileSizeBuffer = ""
    
    #create a buffer for the header size
    fileSizeBuffer = recvAll(socket, 10)

    try:
        fileSize = int(fileSizeBuffer)
        data = recvAll(socket, fileSize)

    except:
        pass
        
    return data

