#map
numbers = [1,2,3,4,5]
numbersSquared = list(map(lambda x: x**2,numbers))

# for i in numbers:
#     numbersSquared.append(i*i)

print(numbersSquared)

#filter
numbersFiltered = list(filter(lambda x: x>2,numbers))
print(numbersFiltered)

#reduce
from functools import reduce
numbersFactorial =  reduce(lambda x,y:x*y,numbers)
print(numbersFactorial)