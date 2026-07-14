import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                username = input("Enter your username: ")
                client.send(username.encode())
            else:
                print("\n" + message)

        except:
            print("\nDisconnected from server.")
            break


def write():
    while True:
        message = input()

        if message.strip().lower() == "/quit":
            client.send("/quit".encode())
            client.close()
            print("You left the chat.")
            break

        client.send(message.encode())


receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

write_thread.join()