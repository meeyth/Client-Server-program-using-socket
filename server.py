import socket
import threading

HEADER = 64
PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
SOCKET_ADDR = (IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SOCKET_ADDR)


def receiveMessage(sender_conn, sender_addr, receiver_conn):
    connected = True
    while connected:
        msg_length = sender_conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = sender_conn.recv(msg_length)
            if msg.decode(FORMAT) == DISCONNECT_MESSAGE:
                sendMessage(receiver_conn, DISCONNECT_MESSAGE.encode(FORMAT))
                print(f"[DISCONNECTING]...{sender_addr}")
                print(f"[DISCONNECTED]...{sender_addr}")
                break
            else:
                sendMessage(receiver_conn, msg)


def sendMessage(receiver_conn, msg):
    send_length = str(len(msg)).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    receiver_conn.send(send_length)
    receiver_conn.send(msg)


def connectClients(conn1, addr1, conn2, addr2):
    print("[CONNECTING]...")
    print(
        f"[NEW CONNECTIONS] {addr1} & {addr2} are communicating.")

    thread1 = threading.Thread(
        target=receiveMessage, args=(conn1, addr1, conn2))
    thread2 = threading.Thread(
        target=receiveMessage, args=(conn2, addr2, conn1))
    thread1.start()
    thread2.start()
    print(f"[ACTIVE CONNECTIONS] {(threading.activeCount() - 2)}")


def main():
    server.listen()
    print(f"[LISTENING] Server is listening {IP}")

    while True:
        conn1, addr1 = server.accept()
        conn2, addr2 = server.accept()
        thread = threading.Thread(
            target=connectClients, args=(conn1, addr1, conn2, addr2))
        thread.start()


if __name__ == "__main__":
    print("[STARTING] server is starting...")
    main()
