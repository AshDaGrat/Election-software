import eel
import auth
import socket

eel.init("/Users/ayaan/Documents/ElectionSoftware/Election-software/src/web")

vDict = {}


@eel.expose
def votingDict(post, candidate):
    vDict[post] = candidate


@eel.expose
def test(a):
    print(a)

    """if auth.valid_usn(input_val, "../data/done.xlsx"):
        return 1  # check for if they have already voted
    if not (auth.valid_usn(input_val, "../data/usn.xlsx")):
        return 2  # check for invalid USN
    else:
        # auth.add_to_excel(input_val, "data/done.xlsx")
        return 3"""


HEADER = 256
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
           'ass-g': 'bill sinby',
           'ic-p': 'the abhuraj',
           'ic-vp': 'nigin',
           'ic-sec': 'therila',
           'ic-t': 'pankti'
           }

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))


@eel.expose
def login(input_val):
    input_val = int(input_val)
    print(input_val)
    send(str([0, input_val]))
    x = client.recv(HEADER).decode(FORMAT)
    x = eval(x)
    # print(type(x))
    # print(int(x[1]))
    return int(x[1])


@eel.expose
def wannaVote(input_val):
    if input_val == "forfeit":
        return 0
    elif input_val == "yes":
        return 1
    else:
        return 2


# Start the index.html file
eel.start("index.html")

# send(str(CHOICES))
