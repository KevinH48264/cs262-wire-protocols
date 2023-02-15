import socket
import _thread
import sys
import os
import subprocess

'''
accounts = { username: conn_var }
queues = { username: [msgs] } 
'''
accounts = {}
queues = {}

# implement as txt file to retrieve from in the future
def init():
    # read from txt files accounts and queues
    pass

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = "10.250.253.162"
        port = 9998
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)
def socket_accept():
    while True:
        conn, address = s.accept()
        print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))

        # allow for multiple connections to be made
        _thread.start_new_thread(receive_commands, (conn, address))
    s.close()

# Send commands to client/victim or a friend
def receive_commands(conn):
    # TODO: Edit this so that user can create account, and the other stuff.
    while True:
        print("hi")
        data = conn.recv(1024)
        input_cmd = data.decode("utf-8")
        res = "Waiting for valid response..."

        # b - allow client to 1. create an account and supply a unique user name
        if 'create_account' in input_cmd:
            res = "create_account"

        # b - allow clients to log in
        if 'log_in ' in input_cmd:

            # k - server delivers undelivered messages to a particular user if they logged in
            check_queue(input_cmd[8:], conn)

        # b - allow client to list accounts by text wildcard

        # k - allow client to send a message to a recipient, and queue if the recipient isn't logged in
        # to send a message: "send_message_to [INSERT RECIPIENT] message: [INSERT MESSAGE]"
        if 'send_message_to ' in input_cmd:
            res = send_message(input_cmd)


        # b- allow client to delete an account

        # k - allow clients to quit connection
        if 'quit' in input_cmd[:4]:
            # mark that the sender has closed their connection
            sender = accounts.keys()[accounts.values().index(conn)]
            accounts[sender] = None

        conn.send(str.encode(res))

def check_queue(user, conn):
    # send messages to user
    for msg in queues[user]:
        conn.send(str.encode(msg))

def send_message(input_cmd, conn):
    # ensure the formatting for sending a message is correct
    if 'message: ' not in input_cmd:
        res = "please send a message using this format: 'send_message_to [INSERT RECIPIENT] message: [INSERT MESSAGE]'"
    
    recipient = input_cmd[17:input_cmd.find("message: ")]
    message = input_cmd[input_cmd.find("message: ") + 9:]

    if recipient in accounts.keys(): 
        # recipient exists
        recipient_conn = accounts[recipient]
        
        if recipient_conn:
            # recipient is online and message can be delivered
            recipient_conn.send(str.encode(message))
        else:
            # recipient is offline and message should be stored in queue
            sender = accounts.keys()[accounts.values().index(conn)]
            queues[recipient] = queues[recipient].append([sender + " sent you a message: " + message])
    else:
        # recipient does not exist
        res = "error: the recipient " + recipient + " does not exist, please have them create an account before you can send a message to them"
    
    return res

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()