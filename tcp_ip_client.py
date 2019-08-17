import socket

#take server name and port no.
host ="localhost"
port =5000

#create a socket at server side using Tcp/ip protocol
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket and port
s.connect((host,port))

#retrieve a msg from server,1024 B at a time
msg=s.recv(1024)

#repeat msg string till msg is not empty

while msg:
    print("Received:", msg.decode())
    msg=s.recv(1024)

s.close()