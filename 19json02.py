import json

with open("users.json") as usersdata:
    data = json.load(usersdata)
    print(data[0]["username"])
    print(data[0]["address"]["street"]) 