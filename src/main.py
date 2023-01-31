import eel
from random import randint
import auth

eel.init("Election-software\\src\\web")

# login
@eel.expose	
def login(input_val):
	print(input_val)
	auth.add_to_excel(input_val, "Election-software\\data\\done.xlsx")
	return auth.valid_usn(input_val, "Election-software\\data\\usn.xlsx")

# Start the index.html file
eel.start("index.html")