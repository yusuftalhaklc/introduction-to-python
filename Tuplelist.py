#tuple
tuplelist = (2,4,6,"Amsterdam")
list = [2,4,6,"Amsterdam"]

# tuplelist[0] = 6  //'tuple' object does not support item assignment//
# Can't change tuple lists
list[0] = 6
print(tuplelist)
print(list)

#output
# (2, 4, 6, 'Amsterdam')
# [6, 4, 6, 'Amsterdam']

