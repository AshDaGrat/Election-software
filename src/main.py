import eel
import auth

eel.init("src/web")

# login
@eel.expose	
def login(input_val):
	print(input_val)
	auth.add_to_excel(input_val, "data\\done.xlsx")
	return auth.valid_usn(input_val, "data\\usn.xlsx")

@eel.expose
def test(a):
	print(a)

# Start the index.html file
eel.start("index.html")