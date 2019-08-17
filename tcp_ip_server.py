import socket

#take server name and port no.
host ="localhost"
port =5000

#create a socket at server side using Tcp/ip protocol
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket and port
s.bind((host,port))

#allow max 1 connection to the socket
s.listen(1),

#wait till client accept the connection
c,addr =s.accept()

print("connection from :",str (addr))

c.send(b"hello there. whats up")
#b is prefix or binary string
msg="see you later"
c.send(msg.encode())

#disconnect from server
c.close()