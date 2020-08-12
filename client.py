import socket, sys, os


# here the client share his files to the server, and open a socket to receive transference requests
def version_0(server_ip, server_port, transfer_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))  # connect to server
    message = "1 " + str(transfer_port) + ' '
    files = [f for f in os.listdir('.') if os.path.isfile(f)]  # get files in current directory
    for f in files:
        message += f + ','
    s.send(message[:-1].encode())  # sends files to server
    s.close()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', transfer_port))  # open server
    server.listen(5)
    while True:
        client_socket, client_address = server.accept()
        file_name = client_socket.recv(1024).decode()  # get file name to be send
        f = open(file_name, 'rb')  # open the file as binary file
        segment = f.read(1024)  # read parts of file
        while segment:  # sending part after part to the client
            client_socket.send(segment)
            segment = f.read(1024)
        f.close()  # close the file
        client_socket.close()


# here the client send a string to server , server return files contain this string
# and the client connect to the client that has this file and request it
def version_1(server_ip, server_port):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))
        search = input("Search: ")
        s.send(('2 ' + search).encode())  # format: 2 [searchString]
        data = s.recv(4096).decode()
        s.close()
        if data == '\n':  # empty
            input("Choose: ")
            continue
        files_info = [(inf.split()[0], inf.split()[1], inf.split()[2]) for inf in data.split(',')]
        files_names = [item[0] for item in files_info]
        files_names.sort()  # sorting with ascending order
        sorted_files_info = []
        for i in files_names:  # sort files information according to sorted files name
            for j in files_info:
                if i == j[0]:
                    sorted_files_info.append(j)
                    files_info.remove(j)
                    break
        counter = 1
        for name in files_names:  # print available to the user
            print(str(counter) + ' ' + name)
            counter += 1
        try:
            choice = int(input("Choose: "))
        except:
            continue
        if 1 <= choice <= len(sorted_files_info):  # in range , else ignore
            transfer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # connect to appropriate client
            transfer_socket.connect((sorted_files_info[choice - 1][1], int(sorted_files_info[choice - 1][2])))
            transfer_socket.send(sorted_files_info[choice - 1][0].encode())  # send file name
            with open(sorted_files_info[choice - 1][0], 'wb') as f:  # create file with the same name
                while True:  # writing
                    segment = transfer_socket.recv(1024)
                    if not segment:
                        break
                    f.write(segment)
            f.close()  # close files
            transfer_socket.close()


def main():
    assert len(sys.argv) == 4 or len(sys.argv) == 5, 'invalid arguments'
    version = int(sys.argv[1])
    assert version == 1 or version == 0, 'invalid arguments'
    if version == 0 and len(sys.argv) != 5:
        raise Exception('invalid arguments')
    if version == 1 and len(sys.argv) != 4:
        raise Exception('invalid arguments')
    if version == 0:
        version_0(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    if version == 1:
        version_1(sys.argv[2], int(sys.argv[3]))


if __name__ == "__main__":
    main()
