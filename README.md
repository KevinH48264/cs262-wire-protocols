Design notebook: https://docs.google.com/document/d/1O02g64RKuSJvuYscbTvHQCIFWnbLA0n8cMBo4fyD09Y/edit?usp=sharing

# Setup Instructions:

## Part 1:

#### 1. Navigate to `cs262-wire-protocols/socket`.

2. Identify the ip address and port number of the computer that will run the server. In `server.py` on lines 23 and 24, set

	``` 
	host = "INSERT YOUR SERVER IP ADDRESS HERE" (e.g. "10.250.109.126")
	port = INSERT YOUR PORT NUMBER HERE (e.g. 9998)
	``` 

In`client.py`, set `server_ip_address` and `port` as the same ip address and port number as in `server.py`, respectively. 


3. Start the server by running the following command in a terminal:

	``` python server.py ```

4. Start the client by running the following command in a separate terminal:

	``` python client.py ```


After following setup instructions above with both a client and server running in two separate terminals, these are the commands to test the server on the client terminal:


1. Create an account. You must supply a unique username.

**Run this command:**

`create_account [USERNAME]`

**Expected result:**

If username is unique: “Account [USERNAME] created!”
If username is not unique: “This username already exists. If this is your account, please log in. If not, create an account with a different username.”


2. List accounts (or a subset of the accounts, by text wildcard).

**Run this command:** `show_accounts [USERNAME AND WILDCARD (optional)]`

**Expected result:**

“[username 1] [username 2] …”

Note: Wildcard is defined here as the regex matching pattern. Example: “k*” means any substring with zero or one occurrence of k. This would match all characters. ke* would match anything with k as the first char.


3. Send a message to a recipient. If the recipient is logged in, deliver immediately; otherwise queue the message and deliver on demand. If the message is sent to someone who isn't a user, return an error message.

**Run this command:** `send_message_to [INSERT RECIPIENT] message: [INSERT MESSAGE]`

**Expected result:**

If recipient is logged in: 

SENDER receives: “message successfully sent to [RECIPIENT]”
RECIPIENT receives: “[SENDER] sent you a message: [MESSAGE]“

If recipient is not logged in: 

SENDER receives: “message will be sent to [RECIPIENT] when they log in”
RECIPIENT receives: “[SENDER] sent you a message: [MESSAGE]“

If recipient isn’t a user:

SENDER receives: “error: the recipient [RECIPIENT] does not exist, please have them create an account before you can send a message to them”


4. Deliver undelivered messages to a particular user.

Assuming you have SENDER and RECIPIENT clients, run the following command: 

**Run this command:** [in RECIPIENT terminal] `quit`

**Expected result:**

“successfully quit / logged off”

**Run this command:** [in SENDER terminal] `send_message_to [RECIPIENT] message: [INSERT MESSAGE]`

**Expected result:**

SENDER receives: "message will be sent to [RECIPIENT] when they log in"

**Run this command:** [in RECIPIENT terminal] `log_in [RECIPIENT]`

**Expected result:**

RECIPIENT receives: “[RECIPIENT] is successfully logged in!”
RECIPIENT receives: “[SENDER] sent you a message: [MESSAGE]“


5. Delete an account. You will need to specify the semantics of what happens if you attempt to delete an account that contains an undelivered message.

**Run this command:** `delete_account [username]`

**Expected result:** 

“The account [username] has been successfully deleted.”


# Part 2:

1. Navigate to `cs262-wire-protocols/grpc`.

2. Identify the ip address and port number of the computer that will run the server. In `server.py` on lines 9 and 10, set

	``` 
	ip = "INSERT YOUR SERVER IP ADDRESS HERE" (e.g. "10.250.109.126")
	port = INSERT YOUR PORT NUMBER HERE (e.g. 9998)
	``` 

In`client.py`, set `server_ip_address` and `port` as the same ip address and port number as in `server.py`, respectively. 


3. Start the server by running the following command in the terminal:

	``` python server.py ```

4. Start the client by running the following command in the terminal:

	``` python client.py ```