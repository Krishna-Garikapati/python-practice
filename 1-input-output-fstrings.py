#Question 1: Basic Input/Output
name = input("What is your name? ")
age = input("What is your age? ")
print("Hello " + name + "! You are " + age + " years old.")

#alternative is f strings
print(f"Hello {name}! You are {age} years old.")

#another alternative .format()
count_a = 3
name = "Krishna"

print("{0} has {1} a's".format(name, count_a))

#for debugging just add breakpoints and run debugger