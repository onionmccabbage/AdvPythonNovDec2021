import socket # lets us open a socket to listen to requests

def myServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now we can configure our server
    param_t = ('localhost', 9874)
    server.bind( param_t )
    # begin listening for requests
    server.listen(4) # max number of connections
    print('The server is listening on port {} on {}'.format(param_t[1], param_t[0]))
    # we need a run loop so we can respond to requests continuously
    while True:
        # unpack any request we may have received
        (client, addr) = server.accept()
        print(client, addr)
        # read data from the client request
        buf = client.recv(1024) # read the first 1024 bytes from the client request
        print('Server received {}'.format(buf))
        # decide what to do about this.... in this case, just send it back CAPITALIZED
        client.send( buf.upper() ) # this does NOT alter buf
        # we can provide a way to quit the server
        if buf == b'quit': 
            server.close()
            break # this breaks out of the current loop

if __name__ == '__main__':
    myServer() # get our server up and running