import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen()

def accept_coonection(server_socket):
    while True:
        client_socket, address = server_socket.accept()
        print('Connection from', address)
        send_message(client_socket)

def send_message(client_socket):
    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)

    client_socket.close()

if __name__=='__main__':
    accept_coonection(server_socket)