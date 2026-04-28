# Write a function check_even(num)
# Return "Even" or "Odd"

# Write a function is_eligible(age)
# If age ≥ 18 → return "Eligible"
# Else → "Not Eligible"

# Write a function check_range(num)
# If number is between 10 and 50 → "In Range"
# Else → "Out of Range"


#functions
def check_even(num):
    if (num%2==0):
        result="The given number is even"
    else:
        result="The given number is odd"
    return result

def is_eligible(age):
    if(age>=18):
        result ="Eligible"
    elif(age<0):
        result="Please enter correct age"
    else:
        result ="Not Eligible"
    return result

#As functions have local scope two functions can have same variable names
def check_range(num):
    if (num>10 and num<50):
        result = "in range"
    else:
        result = "Out of range"
    return result


#main program
my_age = int(input("Enter your age: "))
my_number = int(input("Enter your number: "))

print(is_eligible(my_age))
print(check_even(my_number))
print(check_range(my_number))
