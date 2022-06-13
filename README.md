# A Client Server program using socket module in python
<!-- 
![The flow chart of server-client.](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg) -->
## Wondering what socket is?

Here is your answer, _SOCKET_ is a address made up of two independent entity first one is _IP_ address and second one is the _PORT_ number it is a 48 bits address where the first 32 bits represent a ip address and last 16 bits represent the port number.

### ___Don't forget to learn these socket functions before using _SOCKET_ module___

- __gethostname()__ _Returns the host name._
- __gethostbyname(host_name)__ _Takes host name as an argument and returns ip address of that host._
- __socket(socket.AF_INET, socket.SOCK_STREAM)__ _Create a server or client and returns a socket object._
- __bind(SOCKET_ADDR)__ _Method which binds it to a specific IP and port so that it can listen to incoming requests on that IP and port._
- __listen()__ _Listen method which puts the server into listening mode, this allows the server to listen to incoming connections_
- __accept()__ _The accept method initiates a connection with the client._
- __send(message)__ _Sends the messege in encoded format._
- __recv(msg_length_in_bytes)__ _Takes messege length as an argument and receives messege of that length._
- __close()__ _Close method closes the connection with the client._
- __encode(FORMAT)__ _Takes a format and __encodes__ a normal string into a byte string._
- __decode(FORMAT)__ _Takes a format and __decodes__ a byte string into a normal string._

### ___Some unique values of socket module___  

- __socket.AF_INET__ _AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses)._
- __socket.SOCK_STREAM__ _SOCK_STREAM. Provides sequenced, two-way byte streams with a transmission mechanism for stream data._

### ___How socket works?___

Follow the reference [`image`](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg).

In _` server.py `_ and _` client.py `_ we got port address by creating a tuple of ip address and port number.  
In code `SOCKET_ADDR = (IP, PORT)` where we got the ip address using two functions of socket module `IP = socket.gethostbyname(socket.gethostname())`

In these python project I made a server _` server.py `_  and  _` client.py `_ cli based programmes, but here we have two client programmes `tom.py` and `jerry.py` to communicate with each other first run the _` server.py `_ file when it's running run both client programmes one after another in different command prompt window.

__congratulations, you got it now you are ready to communicate between clients.__
