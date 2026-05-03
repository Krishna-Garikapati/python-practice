# Q3 — Method Overriding (Inheritance)

# 👉 Question

# Create:

# Parent class Animal → method speak() → "Some sound"
# Child class Dog → override → "Bark"

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

a = Animal()
d = Dog()

print(a.speak())
print(d.speak())