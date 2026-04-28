#Print numbers from 1 to 10 using while
num=0
while (num<10):
    num=num+1
    print(num)

#Print numbers from 10 to 1 using while
num=11
while(num>1):
    num=num-1
    print(num)

#Keep asking user for input until they enter 0
user_input = int(input("Enter a number: "))
while(user_input != 0):
    user_input = int(input("Enter number again: "))
print("you entered correct number")

   