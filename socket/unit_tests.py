import socket, select
import sys
from server.py import main
import _thread


# insert the server computer's IP address and port here
host = '10.250.253.162:9955'
port = 9955

# run the server
_thread.start_new_thread(main, (host,))

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server host and port
s.connect((host, port))

# Waiting for response from server that there was a successful connection
print(str(s.recv(1024),"utf-8"), end="")

# Create account
create_account_test = ["create_account kevin", "create_account brandon"]
create_account_answer = ["account_created", "account_created"]

for i in range(len(create_account_test)):
    test, answer = create_account_test[i], create_account_answer[i]

    s.send(str.encode(test))
    response = str(s.recv(1024),"utf-8")    

    assert(response == answer)


# # List accounts
# list_account_test = ['create_account kevin', 'create_account kevin1', 'show_accounts', 'show_accounts k*']

# # stop connection by using Ctrl+C, otherwise continually listen to the server once connected
# while True:
#     # listen to the socket or stdin for keyboard inputs.
#     ready, _, _ = select.select([s.fileno(), sys.stdin.fileno()], [], [], 0.1)
    
#     # once ready, check if the response is from a keyboard input (stdin) or server (socket connection)
#     if ready:
#         if s.fileno() in ready:
#             # decode and print the encoded socket message
#             response = str(s.recv(1024),"utf-8")
#             print(response, end="")

#         elif sys.stdin.fileno() in ready:
#             # read the keyboard input
#             cmd = sys.stdin.readline()
            
#             # if there is a command prompt, send it to the socket and wait for a server response before printing it and continuing
#             if cmd:
#                 s.send(str.encode(cmd))
#                 response = str(s.recv(1024),"utf-8")
#                 print(response, end="")