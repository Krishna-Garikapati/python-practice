#Print numbers from 1 to 10

for counter in range(1, 11):
        print(counter)

#Print numbers from 10 to 1
for counter in range(10,0,-1):
        print(counter)

#Print only even numbers from 1 to 20
for counter in range(1,21):
    if(counter%2 == 0):
        print(counter)

#Print the sum of numbers from 1 to 10
result=0
for counter in range(1,11):
    result=result+counter
print(result)

