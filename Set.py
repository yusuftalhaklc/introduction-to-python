#Set
studentsSet = {"yusuf","talha","arda","ayşe","esma"}
for student in studentsSet:
    print(student)           # it is outputing randomly
print("yusuf" in studentsSet)
studentsSet.update(["merve","mert","selin"])
print(studentsSet)
studentsSet.remove("merve")
studentsSet.discard("merve") # do not disturb command prompt
studentsSet.pop()
print(studentsSet)
del studentsSet

print("----- set union -----")
#set union
setA = {1,2,3,4,5}
setB = {1,3,4,6,7}

print(setA | setB)
print(setA.union(setB))

print("----- set intersection -----")
#set intersection
print(setA & setB)
print(setA.intersection(setB))

print("----- set difference -----")
#set difference
print(setA - setB)
print(setB.difference(setA))

print("----- set symmetric difference-----")
#set symmetric difference
print(setA ^ setB)
print(setB.symmetric_difference(setA))

#output
# esma
# ayşe
# yusuf
# talha
# arda
# True
# {'merve', 'esma', 'ayşe', 'yusuf', 'mert', 'talha', 'selin', 'arda'}
# {'ayşe', 'yusuf', 'mert', 'talha', 'selin', 'arda'}
# ----- set union -----
# {1, 2, 3, 4, 5, 6, 7}
# {1, 2, 3, 4, 5, 6, 7}
# ----- set intersection -----
# {1, 3, 4}
# {1, 3, 4}
# ----- set difference -----
# {2, 5}
# {6, 7}
# ----- set symmetric difference-----
# {2, 5, 6, 7}
# {2, 5, 6, 7}