import socket
import threading
import json

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server Started...")

clients = []


def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                pass


def handle_client(client):

    while True:

        try:

            message = client.recv(1024)

            if not message:
                break

            broadcast(message, client)

        except:
            break

    clients.remove(client)
    client.close()


while True:

    client, address = server.accept()

    print("Connected:", address)

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,),
        daemon=True
    )

    thread.start()