import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server= 'www.ekovation.com'

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(0,50):
    if pscan(x):
        print('your port', x,'is open')

    else:
        print('your port',x,'is close')

