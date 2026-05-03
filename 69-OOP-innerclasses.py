# Q1 — Basic Inner Class

# 👉 Question
# Create:

# Person
# inner class Address with city
# print city using inner class

class Person:
    class Address:
        def __init__(self,city):
            self.city=city

oc=Person()
ic=oc.Address("Guntur")

print(ic.city)# or
print(Person().Address("Guntur"))


