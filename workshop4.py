students = ["Yusuf","Talha","Esma","Hakan"]
fileToAppend = open("students.txt","a") # a is append

for s in students:
    fileToAppend.write(s)
    fileToAppend.write("\n")

fileToAppend.close()