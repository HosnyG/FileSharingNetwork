import socket, sys
clients = []


class Client:
    def __init__(self, ip, port, trans_port, files):
        self.ip = ip
        self.trans_port = trans_port
        self.port = port
        self.files = files


# return files where there names include 'search' word
def search_files(search):
    msg = ''
    for client in clients:
        for file in client.files:
            if search in file:
                msg += file+' '+client.ip+' '+str(client.trans_port)+','
    if msg != '':
        msg = msg[:-1]  # without last comma
    msg += '\n'
    return msg


# dealing with requests
def parser(message, ip, port, client_socket):
    tokens = message.split()
    try:
        val = int(tokens[0])
        if val == 1:  # join request
            trans_port = int(tokens[1])  # where the client will receive  transference requests
            files = [file for file in tokens[2].split(',')]  # files name
            clients.append(Client(ip, port, trans_port, files))  # add to clients list
        elif val == 2:  # search request
            msg = '\n'  # initial value
            if len(tokens) > 1:  # if not empty
                msg = search_files(tokens[1])  # get files information appropriate with search key
            client_socket.send(msg.encode())
        else:
            raise Exception("invalid format")
    except:
        raise Exception("invalid format")


def main():
    assert len(sys.argv) == 2, 'invalid arguments'  # just one argument : port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', int(sys.argv[1])))
    server.listen(5)
    while True:
        client_socket, client_address = server.accept()

        data = client_socket.recv(1024).decode()
        parser(data, client_address[0], client_address[1], client_socket)
        client_socket.close()


if __name__ == "__main__":
    main()
