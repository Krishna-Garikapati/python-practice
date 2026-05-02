# 7. Rename self (Concept)
# ❓ Question

# Will this work?

class Student:
    #default constructor, self renamed as abc and this works
    def __init__(abc,name,age):
        abc.name=name
        abc.age=age

#object creation
s1=Student("krishna",25)
print(s1.name,s1.age)