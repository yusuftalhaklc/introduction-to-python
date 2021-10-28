# Substring -- string[start: end: step]
message = "Hello World" # A string

print("first example : " + message[0:6])  #Get the first 6 characters of a string

print("second example : " + message[6:9]) #Get a substring of length 3 from the 7th character of the string

print("third example : " + message[6:])   #Get the last characters from 6

print("fourth example : " + message[-1])  #Get the last character of the string

print("fifth example : " + message[-7:])  #Get the last 7 characters of a string

print("sixth example : " + message[::3])  #Get every other character from a string

#output
# first example : Hello
# second example : Wor
# third example : World
# fourth example : d
# fifth example : o World
# sixth example : HlWl