import socket
import sys
import os
import subprocess
import re

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
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    receive_commands(conn)
    conn.close()

# Send commands to client/victim or a friend
def receive_commands(conn):
    # TODO: Edit this so that user can create account, and the other stuff.
    while True:
        print("hi")
        data = conn.recv(1024)
        input_cmd = data.decode("utf-8")
        res = "Waiting for valid response..."

        # b - allow client to 1. create an account and supply a unique user name
        # Input format should be: create_account [USERNAME]
        if 'create_account' in input_cmd:
            # create_account + space is 15 characters
            username = input_cmd[15:]
            res = create_account(username, conn)

        # b - allow clients to log in
        if 'log_in' in input_cmd:
            # log_in + space is 7 characters
            username = input_cmd[7:]
            res = log_in(username, conn)

        # b - allow client to list accounts by text wildcard
        if 'show_accounts' in input_cmd:
            # show_accounts + space is 13 characters
            username = input_cmd[13:]
            res = show_accounts(username)

        # k - allow client to send a message to a recipient, and queue if the recipient isn't logged in

        # k - server delivers undelivered messages to a particular user if they logged in

        # b - allow client to delete an account
        if 'delete_account' in input_cmd:
            # delete_account + space is 15 characters
            username = input_cmd[15:]
            res = delete_account(username, conn)

        # k - allow clients to quit connection

        conn.send(str.encode(res))


def log_in(username, conn):
    if accounts.has_key(username):
        accounts[username] = conn
        return "{} is successfully logged in!".format(username)
    else:
        return "This account does not exist, but the username is available. Please create an account first."

def create_account(username, conn)
    if accounts.has_key(username):
        return "This username already exists. If this is your account, please log in. If not, create an account with a different username."
    else:
        accounts[username] = conn
        queues[username] = []
        return "account_created"

def delete_account(conn)
    try:
        account_to_be_deleted = accounts.keys()[accounts.values().index(conn)]

    except: ValueError:
        return "You are currently not logged in. Please log in first in order to delete your account."

    accounts.pop(account_to_be_deleted)
    queues.pop(account_to_be_deleted)
    return "The account {} has been successfully deleted.".format(account_to_be_deleted)

def show_accounts(search_input)
    regex = re.compile(search_input)
    matches = [string for string in accounts.keys() if re.match(regex, string)]
    return matches


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()