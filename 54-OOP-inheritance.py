# Q3. Constructor + super()

# Create a parent class Person with constructor printing "Parent".
# Create child class Student that calls parent constructor and prints "Child".

#parent class
class Parent():
    def __init__(self):
        print("Parent is")

#child class
class Student(Parent):
    def __init__(delf):
        #calling parent constructor using super()
        super().__init__() #returns Parent is as output
        print("child is")

#object creation
s1=Student()