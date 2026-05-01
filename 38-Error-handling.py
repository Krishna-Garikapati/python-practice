# Q4. Multiple Exceptions
try:
    num=int("abc")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")