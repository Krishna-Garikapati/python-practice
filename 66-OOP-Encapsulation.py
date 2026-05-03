# Q1 — Basic Private Property

# 👉 Question
# Create a class Person with:

# private variable __name
# method get_name()

class Person:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    
#object
p1=Person("Krishna")
print(p1.get_name())
