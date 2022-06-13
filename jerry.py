import socket
import threading


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
IP = socket.gethostbyname(socket.gethostname())
SOCKET_ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SOCKET_ADDR)


def sendMessage():
    while True:
        message = input("[ENTER TEXT] > ")
        message = DISCONNECT_MESSAGE if not message else message
        message = message.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        if message.decode(FORMAT) == DISCONNECT_MESSAGE:
            break


def receiveMessage():
    while True:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            message = client.recv(msg_length).decode(FORMAT)
            print('Message received > ', message)
            if message == DISCONNECT_MESSAGE:
                break


def main():
    send_thread = threading.Thread(
        target=sendMessage)
    receive_thread = threading.Thread(
        target=receiveMessage)
    send_thread.start()
    receive_thread.start()
    send_thread.join()
    receive_thread.join()
    client.close()
    print("Connection Closed!")


if __name__ == "__main__":
    main()
