#Write a program:

# Take marks
# If marks ≥ 90 → "A"
# Else if ≥ 70 → "B"
# Else → "C"

marks = float(input("Please enter your marks: "))

if(0<=marks and marks<=100):
   
    if(100>= marks >= 90):
        print("You got A!!!")
    elif(90> marks >=70):
        print("You got B")
    else:
        print("you got C")
else:
    
    print("Enter the marks between 0-100")
    
