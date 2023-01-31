import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
CHOICES = {'usn': 100212,
           'spl-b': 'raju',
           'spl-g': 'kaju',
           'cs-b': 'gaju',
           'cs-g': 'ayo',
           'ss-b': 'kalia',
           'ss-g': 'dholu',
           'aspl-b': 'bholu',
           'aspl-g': 'priti bala',
           'acs-b': 'varnika',
           'acs-g': 'saswath',
           'ass-b': 'bill cosby',
           'ass-g': 'bill sinby'}
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send(str(CHOICES))
