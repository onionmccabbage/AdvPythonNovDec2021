import socket
import sys

def myClient():
    # open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874)
    # try to connect to our server
    sock.connect(param_t)
    # send a message to the server
    if len(sys.argv) > 1: # check if a sys arg variable was provided
        # take all sys arg variables and concatenate them
        msg = ' '.join(sys.argv[1:])
    else:
        msg = 'dfault message'
    sock.send( msg.encode() ) # use the default URL encoding
    # handle any response from the server
    res = sock.recv(1024) # receive the first 1024 bytes
    print(res)
    # clean up
    sock.close()

if __name__ == '__main__':
    myClient() # get our client running