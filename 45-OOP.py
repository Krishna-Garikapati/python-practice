# 2. Constructor + Attributes
# ❓ Question

# Create a class Student with name and age using constructor.
class Student:
    #default constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

#object creation
s1=Student("krishna",25)
print(s1.name,s1.age)