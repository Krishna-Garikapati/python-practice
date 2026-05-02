# 3. Method
# ❓ Question

# Add a method display() to print student details.

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
s1.display()