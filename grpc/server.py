import re
import grpc
import re
from concurrent import futures
import chat_pb2
import chat_pb2_grpc


ip = "10.250.253.162"
port = "9999"

def check_queue(user, conn):
    # send messages to user
    print(queues[user])
    for msg in queues[user]:
        conn.send(str.encode(msg))
        queues[user].remove(msg)


class ChatServicer(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        self.accounts = {}
        self.queues = {}

    def CreateAccount(self, request, context):
        username = request.request[15:].strip("\n")
        if username in list(self.accounts.keys()):
            return chat_pb2.Response(response="This username already exists. If this is your account, please log in. If not, create an account with a different username.") 
        else:
            self.accounts[username] = context.peer()
            self.queues[username] = []
            return chat_pb2.Response(response="Account {} created!".format(username)) 

    def LogIn(self, request, context):
        username = request.request[7:].strip("\n")
        if username in list(self.accounts.keys()):
            self.accounts[username] = context.peer()

            print("User {} logged in!".format(username))
            return chat_pb2.Response(response="{} is successfully logged in!".format(username))
        else:
            return chat_pb2.Response(response="This account does not exist, but the username is available. Please create an account first.")

    def SendMessage(self, request, context):
        recipient = request.request[16:request.request.find("message: ") - 1]
        message = request.request[request.request.find("message: ") + 9:]

        if recipient not in list(self.accounts.keys()):
            return chat_pb2.Response(response="error: the recipient " + recipient + " does not exist, please have them create an account before you can send a message to them")

        elif self.accounts[recipient] is None:
            # recipient is offline and message should be stored in queue
            sender = list(self.accounts.keys())[list(self.accounts.values()).index(context.peer())]
            self.queues[recipient].append(sender + " sent you a message: " + message)
            return chat_pb2.Response(response="message will be sent to {} when they log in".format(recipient))

        else:
            sender = list(self.accounts.keys())[list(self.accounts.values()).index(context.peer())]
            self.queues[recipient].append(sender + " sent you a message: " + message)            
            return chat_pb2.Response(response="message successfully sent to {}".format(recipient))

    def ShowAccounts(self, request, context):
        print("Request content:", request.request)
        print("Accounts: ", list(self.accounts.keys()))
        search_input = request.request[14:].strip("\n")
        print(search_input)
        regex = re.compile(search_input)
        matches = []
        matches = [string for string in list(self.accounts.keys()) if re.match(regex, string) is not None]
        final_accounts = ""
        for i in range(len(matches)):
            final_accounts += matches[i] + "\n"
        return chat_pb2.Response(response=final_accounts)


    def DeleteAccount(self, request, context):
        try:
            account_to_be_deleted = list(self.accounts.keys())[list(self.accounts.values()).index(context.peer())]
        
        except ValueError:
            return chat_pb2.Response(response="You are currently not logged in. Please log in first in order to delete your account.")

        self.accounts.pop(account_to_be_deleted)
        self.queues.pop(account_to_be_deleted)
        return chat_pb2.Response(response="The account {} has been successfully deleted.".format(account_to_be_deleted))

    def ReceiveMessage(self, request, context):
        try:
            receiving_user = list(self.accounts.keys())[list(self.accounts.values()).index(context.peer())]
        except:
            return chat_pb2.Response(response="")
        messages = self.queues[receiving_user]
        final_messages = ""
        if len(messages) > 0:
            for i in range(len(messages)):
                final_messages += messages[i] + "\n"

            # Empty the queue after all messages have been sent
            self.queues[receiving_user] = []
            return chat_pb2.Response(response=final_messages)

        else:
           return chat_pb2.Response(response="")

    def LogOut(self, request, context):
        print(context.peer())
        print("account keys: ", list(self.accounts.keys()))
        print("account values: ", list(self.accounts.values()))
        username = list(self.accounts.keys())[list(self.accounts.values()).index(context.peer())]
        self.accounts[username] = None
        return chat_pb2.Response(response="successfully quit / logged off")


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port(ip + ":" + port)
    server.start()
    print('Server is running...')
    server.wait_for_termination()