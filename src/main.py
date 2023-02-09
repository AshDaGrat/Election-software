import eel
import auth
import socket

eel.init("web")

vDict = {'USN':None}


@eel.expose
def votingDict(post, candidate):
    vDict[post] = candidate
    print(vDict)


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


HEADER = 512
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.14"
ADDR = (SERVER, PORT)

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


@eel.expose
def submitVote():
    global vDict
    send(str([2, vDict]))
    vDict = {}


@eel.expose
def forfeit():
    global vDict
    send(str([3, vDict['USN']]))
    vDict = {}

# Start the index.html file
eel.start("index.html")

# send(str(CHOICES))
