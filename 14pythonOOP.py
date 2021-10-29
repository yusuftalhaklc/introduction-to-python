class Math:
    def __init__(self,num1,num2):
        print("Çalıştı")
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        return self.num1 + self.num2        
    
    def subtraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2    

def printmathclass():
    math = Math(2,3)
    math2 = Math(3,4)
    print (math.multiplication())

class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

class Worker(Person):
    def __init__(self,salary) :
        self.salary = salary

class Customer(Person):
    def __init__(self,creditcardnumber) :
        self.creditcardnumber = creditcardnumber

yusuf = Worker()
talha = Customer()
