import eel
import auth

eel.init("src\\web")

# login
@eel.expose	
def login(input_val):
	input_val = int(input_val)
	print(input_val)
	if auth.valid_usn(input_val, "data/done.xlsx"): return 1 #check for if they have already voted
	if not(auth.valid_usn(input_val, "data/usn.xlsx")): return 2 #check for invalid USN
	else:
		auth.add_to_excel(input_val, "data/done.xlsx")
		return 3


@eel.expose
def test(a):
	print(a)

# Start the index.html file
eel.start("index.html")