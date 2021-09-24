import socket
from select import select

to_monitoring = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen()

def accept_coonection(server_socket):
    client_socket, address = server_socket.accept()
    print('Server: Connection from', address)
    to_monitoring.append(client_socket)

def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'server response: Hello my first client!\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitoring, [], []) #read, write, error

        for sock in ready_to_read:
            if sock is server_socket:
                accept_coonection(sock)
            else:
                send_message(sock)

if __name__=='__main__':
    to_monitoring.append(server_socket)
    event_loop()
