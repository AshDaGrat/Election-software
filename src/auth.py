import pickle

def valid_usn(usn, file_path="data/usn.dat"):
    data = pickle.load(open(file_path, "rb"))
    if int(usn) in data["data"]:
        return True
    else:
        return False

def done(usn, file_path="data/done.dat"):
    data = pickle.load(open(file_path, "rb"))
    if int(usn) in data["data"]:
        return True
    else:
        return False

def addDone(usn, file_path="data/done.dat"):
    fr = open(file_path, "rb")
    data = pickle.load(fr)
    data["data"].append(int(usn))
    with open(file_path, "wb") as f:
        pickle.dump(data, f)