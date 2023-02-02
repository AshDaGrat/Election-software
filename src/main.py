import eel
import auth
import socket

eel.init("src\\web")

# login
@eel.expose	
def login(input_val):
	input_val = int(input_val)
	print(input_val)
	if auth.valid_usn(input_val, "data/done.xlsx"): return 1 #check for if they have already voted
	if not(auth.valid_usn(input_val, "data/usn.xlsx")): return 2 #check for invalid USN
	else:
		#auth.add_to_excel(input_val, "data/done.xlsx")
		return 3


@eel.expose
def test(a):
	print(a)

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.129.98"
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
           'ic-p' : 'the abhuraj',
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
    print(client.recv(2048).decode(FORMAT))
    
# Start the index.html file
eel.start("index.html")

#send(str(CHOICES))