'''
To run, go to socket/ directory and run 'pytest'
Note: use the prefix "text_" when naming the function so that it is picked up by pytest
'''

import socket
import _thread
from server import run_server, host, port

# run the server in background
_thread.start_new_thread(run_server, ())

# test create account
def test_create_account():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the create_account message
    message = "create_account bob"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")

    assert(response == "account_created\n")

# test when the account name is not unique
def test_create_account_non_unique():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the create_account message
    message = "create_account bob"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")

    assert(response == "This username already exists. If this is your account, please log in. If not, create an account with a different username.\n")