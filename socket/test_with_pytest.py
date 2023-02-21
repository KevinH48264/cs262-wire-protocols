'''
To run, go to socket/ directory and run 'pytest'
Note: use the prefix "test_" when naming the function so that it is picked up by pytest
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
    client_socket.close()
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
    client_socket.close()
    assert(response == "This username already exists. If this is your account, please log in. If not, create an account with a different username.\n")


# test create account
def test_create_second_unique_account():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the create_account message
    message = "create_account kevin"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")
    client_socket.close()
    assert(response == "account_created\n")

def test_show_accounts():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the show_accounts message
    message = "show_accounts"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")
    client_socket.close()
    assert(response == "bob kevin \n")


# test create account
def test_send_message_to_valid_account():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the log_in message
    message = "log_in bob"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")

    # send the sent_message_to message
    message = "send_message_to kevin message: hello kevin"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")
    client_socket.close()
    assert(response == "message successfully sent to kevin\n")

# test create account
def test_send_message_to_non_existent_account():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the log_in message
    message = "log_in bob"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")

    # send the sent_message_to message
    message = "send_message_to james message: hello james"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")
    client_socket.close()
    assert(response == "error: the recipient james does not exist, please have them create an account before you can send a message to them\n")

# test create account
def test_quit():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the log_in message
    message = "log_in kevin"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")

    # send the quit message
    message = "quit"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")

    client_socket.close()
    assert(response == "successfully quit / logged off\n")


# test create account
def test_send_message_when_logged_off():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the log_in message
    message = "log_in bob"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")

    # send the sent_message_to message 
    message = "send_message_to kevin message: hey kevin"
    client_socket.send(str.encode(message))

    # store the response
    response_offline = str(client_socket.recv(1024),"utf-8")

    # send the log_in message which should automatically load bob's message to kevin
    message = "log_in kevin"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")
    client_socket.close()
    assert(response_offline == "message will be sent to kevin when they log in\n")
    assert(response == "bob sent you a message: hey kevin")



# test create account
def test_delete_account():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the create_account message
    message = "log_in kevin"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")
    
    # send the create_account message
    message = "delete_account kevin"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")
    client_socket.close()
    assert(response == "The account kevin has been successfully deleted.\n")


def test_show_accounts_after_deletion():
    global host
    global port

    # create a client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # receive the welcome message
    client_socket.recv(1024).decode()

    # send the show_accounts message
    message = "show_accounts"
    client_socket.send(str.encode(message))

    # store the response
    response = str(client_socket.recv(1024),"utf-8")
    client_socket.close()
    assert(response == "bob \n")
