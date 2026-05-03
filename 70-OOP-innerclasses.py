# Q2 — Inner Class Used Inside Outer Class

# 👉 Question
# Create:

# Student with name
# inner class Laptop with brand
# print both

class Student:
    def __init__(self,name):
        self.name=name
    class Laptop:
        def __init__(self,brand):
            self.brand=brand

#object1
s1=Student("krishna")
l1=s1.Laptop("Dell")

print(s1.name,l1.brand)

#or you do as below
class Student:
    def __init__(self, name, brand):
        self.name = name
        self.laptop = self.Laptop(brand)

    def show(self):
        print("Name:", self.name)
        self.laptop.show()

    class Laptop:
        def __init__(self, brand):
            self.brand = brand

        def show(self):
            print("Laptop:", self.brand)

s = Student("Krishna", "HP")
s.show()