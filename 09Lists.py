#list
print("---- STUDENT ----")
students = ["Yusuf","Talha"]
print(students[1])

#append
print("---- APPEND ----")
students.append("Arda")
print(students[2])

#remove
print("---- REMOVE ----")
students.remove("Arda")
print("students[2] WILL BE SHOWING ERROR")
print("---- CITIES ----")
cities = list(("New york","Los Angelas"))
print(cities)

#count
print("---- COUNT ----")
print(cities.count("New york"))
print("index of new york : " ,cities.index("New york"))

#pop like remove
print("---- POP ----")
cities.pop(1)
print(cities)

#insert
print("---- INSERT ----")
cities.insert(1,"Los Angelas")
print(cities[1])

#reverse 
print("---- REVERSE ----")
cities.reverse();
print(cities)

#copy
print("---- COPY ----")
cities2 = cities.copy()
print(cities2)

#extend
print("---- EXTEND ----")
cities.extend(cities2)
print(cities2)

#sort
print("---- SORT ----")
cities.sort()
cities.reverse()
print(cities)

#clear
print("---- CLEAR ----")
print(cities.clear())
print(cities)

#output 
# ---- STUDENT ----
# Talha
# ---- APPEND ----
# Arda
# ---- REMOVE ----
# students[2] WILL BE SHOWING ERROR
# ---- CITIES ----
# ['New york', 'Los Angelas']
# ---- COUNT ----
# 1
# index of new york :  0
# ---- POP ----
# ['New york']
# ---- INSERT ----
# Los Angelas
# ---- REVERSE ----
# ['Los Angelas', 'New york']
# ---- COPY ----
# ['Los Angelas', 'New york']
# ---- EXTEND ----
# ['Los Angelas', 'New york']
# ---- SORT ----
# ['New york', 'New york', 'Los Angelas', 'Los Angelas']
# ---- CLEAR ----
# None
# []