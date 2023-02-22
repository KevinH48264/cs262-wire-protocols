'''
To run, go to this directory and run 'pytest -v'
'''

import grpc
import chat_pb2_grpc
import _thread
from server import run_server, ip, port
from client import create_account, login, show_accounts, send_message_to, delete_account, quit

# run the server in background
_thread.start_new_thread(run_server, ())

# test create account
def test_create_account():
    global ip
    global port

    # create a client socket
    with grpc.insecure_channel(('{}:{}').format(ip, port)) as channel:
        stub = chat_pb2_grpc.ChatServiceStub(channel)

        # send the create_account message
        cmd = "create_account bob"
        res = "Waiting for a valid response... Please see instructions above."
        # if there is a command prompt, send it and wait for a server response before printing it and continuing
        if len(str.encode(cmd)) > 0:
            if 'create_account' in cmd:
                res = create_account(stub, cmd).response
            if 'log_in' in cmd:
                res = login(stub, cmd).response
            if 'show_accounts' in cmd:
                res = show_accounts(stub, cmd).response
            if 'send_message_to' in cmd:
                res = send_message_to(stub, cmd).response
            if 'delete_account' in cmd:
                res = delete_account(stub, cmd).response
            if 'quit' in cmd:
                res = quit(stub, cmd).response

        # store the response
        assert(res == "Account bob created!")

test_create_account()