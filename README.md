Design notebook: https://docs.google.com/document/d/1O02g64RKuSJvuYscbTvHQCIFWnbLA0n8cMBo4fyD09Y/edit?usp=sharing

# Setup Instructions:

## Part 1:

**1.** Navigate to `cs262-wire-protocols/socket`.

**2.** Identify the ip address and port number of the computer that will run the server. In `server.py` on lines 23 and 24, set

	``` 
	host = "INSERT YOUR SERVER IP ADDRESS HERE" (e.g. "10.250.109.126")
	port = INSERT YOUR PORT NUMBER HERE (e.g. 9998)
	``` 

In`client.py`, set `server_ip_address` and `port` as the same ip address and port number as in `server.py`, respectively. 


**3.** Start the server by running the following command in the terminal:

	``` python server.py ```

**4.** Start the client by running the following command in the terminal:

	``` python client.py ```


# Part 2:

**1.** Navigate to `cs262-wire-protocols/grpc`.

**2.** Identify the ip address and port number of the computer that will run the server. In `server.py` on lines 9 and 10, set

	``` 
	ip = "INSERT YOUR SERVER IP ADDRESS HERE" (e.g. "10.250.109.126")
	port = INSERT YOUR PORT NUMBER HERE (e.g. 9998)
	``` 

In`client.py`, set `server_ip_address` and `port` as the same ip address and port number as in `server.py`, respectively. 


**3.** Start the server by running the following command in the terminal:

	``` python server.py ```

**4.** Start the client by running the following command in the terminal:

	``` python client.py ```