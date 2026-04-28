# Write a function student(name, age)
# Return: "Name: <name>, Age: <age>"

# Write a function max_num(a, b)
# Return the larger number (no built-in max())

#functions
def student(name,age):
    return f"Name: {name}, Age: {age}"

def max_num(a,b):
    if(a>b):
        result =a
    elif(b>a):
        result =b
    else:
        result =f"Both {a} and {b} are equal"
    return f"{result} is greater"


#main program
print(student("krishna",20))
print(max_num(10,5))

