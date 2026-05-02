# 4. Multiple Objects
# ❓ Question

# Create 2 objects and print their data.

class Student:
    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    #method
    def display(self):
        print(f"Student name is {self.name},age is {self.age}")

    #object creation
s1=Student("Krishna",29)
s2=Student("Surya",29)
s1.display()
s2.display()