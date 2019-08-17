import socket

# take the server name
host = 'www.google.co.in'

try:
    addr = socket.gethostbyname(host)
    print('IP Address = ', addr)

except:
    print("the website does not exist")
