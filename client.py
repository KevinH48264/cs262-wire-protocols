import socket

# create a socket
s = socket.socket()

# Get the server computer's IP address
server_ip_address = '10.250.253.162'
port = 9998

s.connect((server_ip_address, port))

while True:
    cmd = input()

    if len(str.encode(cmd)) > 0:
        s.send(str.encode(cmd))
        client_response = str(s.recv(1024),"utf-8")
        print(client_response, end="")

