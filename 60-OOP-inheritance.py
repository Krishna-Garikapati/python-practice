# Q9. Multiple Inheritance
# Create two parent classes and one child class inheriting both.

class Parent():
    def display(self):
        print("This is from Parent class")
class Parent1():
    def show(self):
        print("This is from Parent1 class")
class child(Parent,Parent1):
    pass

#object for child
c1=child()
c1.display()
c1.show()
