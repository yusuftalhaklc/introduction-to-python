# w is write 
# a is append
# x is create if you don't have this file
# r is read

f = open("customers.txt") 
#print(f.read())
#print(f.readline())
print("--- READLİNE ---")
for i in f:
    print(i)
f.close()

fileToAppend = open("students.txt","a")
fileToAppend.write("yusuf")


fileToAppend.close()

import os 
if os.path.exists("students.txt"):
    os.remove("students.txt")
else:
    print("File is not exist")

#folder delete
os.rmdir("empty")