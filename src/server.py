import socket
import threading
import pickle
import auth

HEADER = 512
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def write_to_dat(towrite):
    print(type(towrite))
    fr = open("data/recd_data.dat", "rb")
    data = pickle.load(fr)
    data["data"].append(towrite)
    with open("data/recd_data.dat", "wb") as f:
        pickle.dump(data, f)

def forfeitWrite(USN, file_path="data/forfeit.dat"):
    fr = open(file_path, "rb")
    data = pickle.load(fr)
    data["forfeit"].append(USN)
    with open(file_path, "wb") as f:
        pickle.dump(data, f)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            print(f"[{addr}] {msg}")
            msg = eval(msg)
            print(type(msg))
            print(msg)
            if msg[0] == 0:

                if auth.valid_usn(msg[1]) and auth.done(msg[1]):
                    print(str([1, 1]))
                    print(str([1, 1]).encode(FORMAT))
                    conn.send(str([1, 1]).encode(FORMAT)) # check for if they have already voted

                if not (auth.valid_usn(msg[1])):
                    print(str([1, 2]))
                    print(str([1, 2]).encode(FORMAT))
                    conn.send(str([1, 2]).encode(FORMAT))

                if auth.valid_usn(msg[1]) and not auth.done(msg[1]):
                    print(str([1, 3]))
                    print(str([1, 3]).encode(FORMAT))
                    conn.send(str([1, 3]).encode(FORMAT))

            elif msg[0] == 2:
                write_to_dat(msg[1])
                auth.addDone(msg[1]['USN'])

            elif msg[0] == 3:
                print(msg)
                forfeitWrite(int(msg[1]))
                auth.addDone(int(msg[1]))

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