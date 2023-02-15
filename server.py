import socket
import sys
import os
import subprocess



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
        if 'create_account' in input_cmd:
            res = "create_account"

        # b - allow clients to log in

        # b - allow client to list accounts by text wildcard

        # k - allow client to send a message to a recipient, and queue if the recipient isn't logged in

        # k - server delivers undelivered messages to a particular user if they logged in

        # b- allow client to delete an account

        # k - allow clients to quit connection

        conn.send(str.encode(res))


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()