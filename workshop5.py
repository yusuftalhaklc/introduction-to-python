import sys


import sys
errorLog = open("ErrorLog.txt","a")

myList = [7,"Yusuf",0,3,"6"]
for x in myList:
    print(f"Number {x}")
    try:
        result = 1/int(x)
    except ValueError:
        print("Check if you don't enter a number")
        errorLog.write(f"For '{x}' system was showing {sys.exc_info()[0]}\n")
    except ZeroDivisionError:
        print("You cannot divide by Zero")
        errorLog.write(f"For '{x}' system was showing {sys.exc_info()[0]}\n")
    finally:
        print("Operation is over")
    print(result)