import json

data = '{"firstname":"Yusuf","lastname":"Kılıç"}'

y = json.loads(data)

print(y["firstname"])

#json.dumps(myDict) dictionary to json