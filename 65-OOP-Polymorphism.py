# Q5 — Duck Typing

# 👉 Question

# Create:

# Bird → fly()
# Plane → fly()

# Write a function start(obj) that calls .fly()
class Bird:
    def fly(self):
        print("Bird flying")

class Plane:
    def fly(self):
        print("Plane flying")

def start(obj):
    obj.fly()

start(Bird())
start(Plane())