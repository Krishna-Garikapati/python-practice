#Create list:
# Print:
# length
# max
# min
#count how many times 2
#find index of "9" in list
#Add 10 to list → print updated list
#Remove value 2
#Insert 100 at index 2
#sort the list
#reverse the list


numbers = [5,6,9,2,7]
print(len(numbers))
print(max(numbers))
print(min(numbers))

print(numbers.count(2))
print(numbers.index(9))

numbers.append(10)
print(numbers)

numbers.remove(2)
print(numbers)

numbers.insert(2,100)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#Accessing elements
print(numbers[0])
print(numbers[-1])
del numbers[-1]
print(numbers)
numbers[-1] = 101
print(numbers)







