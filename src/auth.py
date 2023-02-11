import json

def valid_usn(usn, file_path="data/usn.json"):
    data = json.load(open(file_path))
    if int(usn) in data["data"]:
        return True
    else:
        return False

def done(usn, file_path="data/done.json"):
    data = json.load(open(file_path))
    if int(usn) in data["data"]:
        return True
    else:
        return False

def addDone(usn, file_path="data/done.json"):
    data = json.load(open(file_path))
    data["data"].append(int(usn))
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)