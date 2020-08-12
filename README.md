# Simple File Sharing Network Between multiple clients

***
in this project , we will build a simple network for sharing files between multiple clients , with TCP based connection . <br>
to do this , we will create two files : _**server.py**_ and _**client.py**_ <br>
the server opens a socket and listens on port he get as main argument . <br>
**<u>note</u> :** the server is only intended to connect between clients , and the actual file transfer will be directly between clients . <br>
the server will handle these requests from clients : <br>

* **join** : client sends this message wants to interested to join to the network . <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; _format_: `1 [port] [files]`  where : <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp; _port_ : the port where the client will listen for files transfer requests . <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp; _files_ :  list of files , separated by comma, which client wants to share. <br>
<br>

* **search** : client sends this message wants to search about a file across the network
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; _format_: 2 [search]`  where : <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp; _search_: full or partial file name . <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; the server sends back to the client a list of files matches the search term <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; besides the clients information they have these files : <br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [Name] [IP] [PORT],...,[Name] [IP] [Port]
<br><br>
### running server and two clients :<br>
<img width="720" height="370" alt="Untitled" src="https://user-images.githubusercontent.com/69496372/89986884-d7f2dc00-dc85-11ea-87cb-2315eb3723c4.png">
<br>

### search and file transferring : <br>
<img width="720" height="370" alt="2" src="https://user-images.githubusercontent.com/69496372/89986886-d9240900-dc85-11ea-9738-d2ea2520e123.png">
<br>

### search and another file tranferring : <br>
<img width="720" height="370" alt="3" src="https://user-images.githubusercontent.com/69496372/89986891-da553600-dc85-11ea-941c-93752092122b.png">
<br>

