# Q7. Combine all (IMPORTANT 💯)
try:
    num=int("10")
    result=10/num
except ZeroDivisionError:
    print("Divide error")
except ValueError:
    print("Invalid input")
else:
    print("Result:", result)
finally:
    print("Execution Finished")


# Q8. Raise Exception.
age=-5
if age<0:
    raise ValueError("Age cannot be negative")

