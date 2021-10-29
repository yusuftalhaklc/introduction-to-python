#dictionary
myDict = {
    "friends" : "amigos",
    "please" :"porfavor"
}
print(myDict)

myDict["friends"] = "amigas"
print(myDict["please"])

del(myDict["friends"])

#output
# {'friends': 'amigos', 'please': 'porfavor'}
# porfavor