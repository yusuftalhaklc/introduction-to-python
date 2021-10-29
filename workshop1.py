#Factorial workshop
def factorial(num):
    toFactorial = 1
    for numFactorial in range(1,(num+1)):
        toFactorial *= numFactorial  
    return toFactorial

num = int(input("Enter a number :"))
if (num < 0) :
    print("factorial of negative number cannot calculate")
else:
    print(factorial(num))