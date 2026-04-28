#Print all elements
nums = [5, 10, 15, 20]
result=0
for value in nums:
    print(value)
    
#Find sum of all elements
for value in nums:
    result=result+value
print(result)

#Print only even numbers from list
for value in nums:
    if(value%2==0):
        print(value)
    
#Count how many numbers are greater than 10
result=0
for value in nums:
    if(value>10):
        result=result+1
print(result)


#Find largest number without using max()
result=0
for value in nums:
    if(value>result):
        result=value
print(result)
     
#Names starting with "A"
names = ["Krishna", "Ava", "John", "Aria"]

for name in names:
    if name.startswith("A"):
        print(name)

#Take 5 numbers from user → store in list
#Then print sum of list

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0
for num in numbers:
    total += num

print("Sum:", total)