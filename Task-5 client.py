# Client.py

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received message: {message}")
        except ConnectionResetError:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5556))

    message_receiver = threading.Thread(target=receive_messages, args=(client,))
    message_receiver.start()

    while True:
        user_input = input("Client message: ")
        client.send(user_input.encode('utf-8'))

if __name__ == "__main__":
    start_client()
