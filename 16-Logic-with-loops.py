#Count how many numbers from 1–50 are even
result=0
for counter in range(1,51):
    if(counter%2==0):
        result=result+1
print(result)

#Find the sum of odd numbers from 1 to 20
result=0
for counter in range(1,21):
    if(counter%2!=0):
        result=result+counter
print(result)

#Print this pattern:
# *
# **
# ***
# ****
# *****

symbol="*"
for counter in range(1,6):
    result=symbol*counter
    print(result)

# Print numbers from 1–20:
# If even → print "Even"
# Else → print "Odd"
for counter in range(1,21):
    if(counter%2==0):
        print(f"{counter} is Even")
    elif(counter%2 !=0):
        print(f"{counter} is Odd")
    else:
        print(f"{counter} is Neither odd nor even")