# Q6. isinstance() Practice

# Check if object of Dog is instance of both Dog and Animal.

# Q7. issubclass() Practice

# Check class relationship between Dog and Animal.

class Animal():
    pass

class Dog(Animal):
    pass

d1=Dog()
print(isinstance(d1,Dog))
print(isinstance(d1,Animal))
print(issubclass(Dog,Animal))