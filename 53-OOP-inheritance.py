# Q2. Add Child Method

# Create a parent class Animal with method eat().
# Create child class Dog with method bark().
# Call both methods.

#parent class
class Animal():
    def eat(self):
        print("All Animals eat")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

A1=Dog()
A1.bark()
A1.eat()