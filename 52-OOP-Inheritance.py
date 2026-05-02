# Q1. Basic Inheritance

# Create a class Person with method show().
# Create a class Student that inherits from Person.
# Call the method using a Student object.

class Person:
    def show(self):
        print("i am a person")

#child class that inherits person
class Student(Person):
    pass

#object creation
s1=Student()
s1.show()
