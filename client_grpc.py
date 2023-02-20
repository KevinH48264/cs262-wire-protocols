import socket, threading, select
import sys

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server computer's IP address
# brandon's server_ip_address = '10.250.253.162'
server_ip_address = '10.250.109.126'
port = 9973

s.connect((server_ip_address, port))

# Waiting for response that we are successfully connected
print(str(s.recv(1024),"utf-8"), end="")

def receive_message(s):
    print("receiving message")
    while True:
        #print("waiting to receive message")
        ready, _, _ = select.select([s], [], [], 0.1)
        if ready:
            client_response = str(s.recv(1024),"utf-8")
            if not client_response:
                break
            print(client_response, end="")
    print("Broke receive")

def send_message(s):
    print("sending message")
    while True:
        #print("waiting for input")
        ready, _, _ = select.select([sys.stdin], [], [], 0.1)
        if ready:
            #cmd = input()
            cmd = sys.stdin.readline()
            if len(str.encode(cmd)) > 0:
                s.send(str.encode(cmd))
                client_response = str(s.recv(1024),"utf-8")
                print(client_response, end="")

            if cmd == "quit":
                s.send(str.encode(cmd))
                break
    print("broke send")

while True:
    sockets_list = [sys.stdin, s]
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == s:
            client_response = str(s.recv(1024),"utf-8")
            if not client_response:
                break
            print(client_response, end="")
        else:
            cmd = sys.stdin.readline()
            if len(str.encode(cmd)) > 0:
                s.send(str.encode(cmd))
                client_response = str(s.recv(1024),"utf-8")
                print(client_response, end="")

            if cmd == "quit":
                s.send(str.encode(cmd))
                break
s.close()


# Create two threads for sending and receiving messages
#receive_thread = threading.Thread(target=receive_message, args=(s,))
#send_thread = threading.Thread(target=send_message, args=(s,))

# Start both threads
#receive_thread.start()
#send_thread.start()

# Wait for both threads to finish
# receive_thread.join()
# send_thread.join()

# while True:
#     cmd = input()
    
#     if len(str.encode(cmd)) > 0:
#         s.send(str.encode(cmd))
#         client_response = str(s.recv(1024),"utf-8")
#         print(client_response, end="")

#     if cmd == "quit":
#         s.send(str.encode(cmd))
#         break