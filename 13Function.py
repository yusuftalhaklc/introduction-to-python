#functions
def greet(name = "Dear"):
    print("Hello "+name)
greet("Yusuf")
greet()

#output
# Hello Yusuf
# Hello Dear  

#function return
def myCalc(num1,num2):
    return (num1+num2)

total = myCalc(3,9)
print(total)

#output
# Hello Yusuf
# Hello Dear
# 12    

#Lambda Function
myCalc2 = lambda num1,num2 : num1+num2
print(myCalc2(9,9))

#output
# 18