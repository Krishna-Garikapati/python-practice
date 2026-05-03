# Q2 — Polymorphism with Function

# 👉 Question

# Create a function make_sound(obj) that calls .sound() on any object.

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def make_sound(obj):
    print(obj.sound())


make_sound(Dog())
make_sound(Cat())

# Why self is NOT used in make_sound
# obj is just a normal parameter
# You can name it anything: obj, animal, x

# What self actually means

# self is only used inside a class method:

# But don’t do that (best practice)

# Using self in a normal function is confusing because: (so here make_sound is normal function with parameters not a class method)

# self implies “this is a class method”
# Other developers will expect it inside a class