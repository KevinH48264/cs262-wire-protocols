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
    return stub.ListAccounts(chat_pb2.Request(request=cmd))

def send_message_to(stub, cmd):
    return stub.SendMessage(chat_pb2.Request(request=cmd))

def delete_account(stub, cmd):
    return stub.DeleteAccount(chat_pb2.Request(request=cmd))

def quit(stub, cmd):
    return stub.LogOut(chat_pb2.Request(request=cmd))

def run():
    with grpc.insecure_channel('{}:{}').format(server_ip_address, port) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        while True:
            # message = stub.ReceiveMessage()
            # if (message):
            #     client_response = str(message.text,"utf-8")
            #     if not client_response:
            #         break
            #     print(client_response, end="")
        
            ready, _, _ = select.select([sys.stdin.fileno()], [], [], 0.1)
            if ready:
                if sys.stdin.fileno() in ready:
                    cmd = sys.stdin.readline()
                    if len(str.encode(cmd)) > 0:
                        if 'create_account' in cmd:
                            create_account(stub, cmd)
                        if 'log_in' in cmd:
                            login(stub, cmd)
                        if 'show_accounts' in cmd:
                            show_accounts(stub, cmd)
                        if 'send_message_to' in cmd:
                            send_message_to(stub, cmd)
                        if 'delete_account' in cmd:
                            delete_account(stub, cmd)
                        if 'quit' in cmd:
                            quit(stub, cmd)
                            break

if __name__ == '__main__':
    run()