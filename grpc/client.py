import socket, threading, select
import grpc
import chat_pb2
import chat_pb2_grpc
import sys

# Get the server computer's IP address
server_ip_address = '10.250.109.126'
port = 9999

def create_account(stub, cmd):
    return stub.CreateAccount(chat_pb2.Request(request=cmd))

def login(stub, cmd):
    return stub.LogIn(chat_pb2.Request(request=cmd))

def show_accounts(stub, cmd):
    return stub.ShowAccounts(chat_pb2.Request(request=cmd))

def send_message_to(stub, cmd):
    return stub.SendMessage(chat_pb2.Request(request=cmd))

def delete_account(stub, cmd):
    return stub.DeleteAccount(chat_pb2.Request(request=cmd))

def quit(stub, cmd):
    return stub.LogOut(chat_pb2.Request(request=cmd))

def run():
    with grpc.insecure_channel(('{}:{}').format(server_ip_address, port)) as channel:
        stub = chat_pb2_grpc.ChatServiceStub(channel)

        print("YOU ARE SUCCESSFULLY CONNECTED TO THE SERVER! Instructions here: 1. create_account [USERNAME] 2. show_accounts [USERNAME (optional)] 3. send_message_to [INSERT RECIPIENT] message: [INSERT MESSAGE] 5. delete_account [username] 6 (extra, logs you in): log_in [USERNAME] 7. (extra, logs you out): quit\n")

        while True:
            message = stub.ReceiveMessage(chat_pb2.Request(request="temp"))
            if (message and message.response):
                print(message.response)
            
            ready, _, _ = select.select([sys.stdin.fileno()], [], [], 0.1)
            if ready:
                if sys.stdin.fileno() in ready:
                    cmd = sys.stdin.readline()
                    res = "Waiting for a valid response... Please see instructions above."
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
                    print(res)

if __name__ == '__main__':
    run()