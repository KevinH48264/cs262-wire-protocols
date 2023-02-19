import socket
import _thread
import re
import grpcio
import re
from concurrent import futures
import chat_pb2
import chat_pb2_grpc

class ChatServicer(chat_pb2_grpc.MessagingServiceServicer):
    def __init__(self):
        self.accounts = {}
        self.queues = {}

    def create_account(self, request, context):
        if request.username in self.accounts:
            context.abort(grpc.StatusCode.ALREADY_EXISTS, 'Account already exists')
        else:
            self.accounts[request.username] = None
            return chat_pb2.Empty()

    def log_in(self, request, context):
        if request.username not in self.accounts:
            context.abort(grpc.StatusCode.NOT_FOUND, 'This account does not exist, but the username is available. Please create an account first.')
        else:
            self.accounts[request.username] = context.peer()
            self.check_queue(request.username, context)
            return chat_pb2.Empty()

    def send_message(self, request, context):
        if request.recipient not in self.accounts:
            context.abort(grpc.StatusCode.NOT_FOUND, 'Recipient not found')
        elif self.accounts[request.recipient] is None:
            sender = next(k for k, v in self.accounts.items() if v == context.peer())
            self.queues.setdefault(request.recipient, []).append(f'{sender} sent you a message: {request.text}')
            return chat_pb2.Empty()
        else:
            recipient_channel = self.accounts[request.recipient]
            stub = chat_pb2_grpc.MessagingServiceStub(recipient_channel)
            stub.send_message(request)
            return chat_pb2.Empty()

    def list_accounts(self, request, context):
        pattern = re.compile(request.pattern)
        accounts = [chat_pb2.Account(username=username) for username in self.accounts if pattern.match(username)]
        return chat_pb2.ListAccountsResponse(accounts=accounts)

    def check_queue(self, user, context):
        for msg in self.queues[user]:
            context.write(chat_pb2.Message(text=msg))
            self.queues[user].remove(msg)

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_MessagingServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server is running...')
    server.wait_for_termination()