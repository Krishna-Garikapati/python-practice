#Generic exception handling
try:
    result=10/0
except:
    print("Cannot divide by zero")

#error specific handling
#zeridivisionerror is built-in class of exceptions in python
try:
    result=10/0
except ZeroDivisionError:
    print("Divide by zero error")

try:
    result=10/0
except ZeroDivisionError as e:
    print("Divide by zero error",e)
