#Basic Polymorphism
# Question

# Create two classes:

# Dog → method sound() → "Bark"
# Cat → method sound() → "Meow"

# Write code to call both using a loop.

class Dog:
    def sound(self):
        print("Dog Barks")

class Cat:
    def sound(self):
        print("Cat meows")

#object
animals = [Dog(),Cat()]

for a in animals:
    a.sound()