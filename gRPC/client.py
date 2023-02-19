# Import necessary packages
import grpc
import messaging_pb2
import messaging_pb2_grpc

# Define the server address
server_address = "localhost:50051"

# Create a gRPC channel and stub
channel = grpc.insecure_channel(server_address)
stub = messaging_pb2_grpc.MessagingServiceStub(channel)

# Define functions to call the gRPC methods
def create_account(username):
    account = messaging_pb2.Account(username=username)
    response = stub.CreateAccount(account)
    return response

def log_in(username):
    account = messaging_pb2.Account(username=username)
    response = stub.LogIn(account)
    return response

def send_message(recipient, text):
    message = messaging_pb2.Message(recipient=recipient, text=text)
    response = stub.SendMessage(message)
    return response

def list_accounts(pattern):
    request = messaging_pb2.ListAccountsRequest(pattern=pattern)
    response = stub.ListAccounts(request)
    return response.accounts

def delete_account():
    response = stub.DeleteAccount(messaging_pb2.Empty())
    return response

# Example usage
username = "example_username"
create_account_response = create_account(username)
print(f"Create account response: {create_account_response}")

log_in_response = log_in(username)
print(f"Log in response: {log_in_response}")

recipient = "example_recipient"
text = "example_text"
send_message_response = send_message(recipient, text)
print(f"Send message response: {send_message_response}")

pattern = "example_pattern"
list_accounts_response = list_accounts(pattern)
print(f"List accounts response: {list_accounts_response}")

delete_account_response = delete_account()
print(f"Delete account response: {delete_account_response}")