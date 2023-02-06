import socket
import threading
import json
import auth

HEADER = 256
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def write_to_json(towrite):
    towrite = eval(towrite)
    data = json.load(open("data/recd_data.json"))
    data["data"].append(towrite)
    with open("data/recd_data.json", "w") as f:
        json.dump(data, f, indent=4)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            #write_to_json(msg)

            print(f"[{addr}] {msg}")
            msg = eval(msg)
            print(type(msg))
            print(msg)
            if msg[0] == 0:
                if auth.valid_usn(msg[1], "/Users/ayaan/Documents/ElectionSoftware/Election-software/data/done.xlsx"):
                    print(str([1, 1]))
                    print(str([1, 1]).encode(FORMAT))
                    conn.send(str([1, 1]).encode(FORMAT))  # check for if they have already voted
                if not (auth.valid_usn(msg[1], "/Users/ayaan/Documents/ElectionSoftware/Election-software/data/usn.xlsx")):
                    print(str([1, 2]))
                    print(str([1, 2]).encode(FORMAT))
                    conn.send(str([1, 2]).encode(FORMAT))
                else:
                    print(str([1, 3]))
                    print(str([1, 3]).encode(FORMAT))
                    conn.send(str([1, 3]).encode(FORMAT))
            else:
                conn.send("Msg received".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()