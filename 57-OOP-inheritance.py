# Q5. Use super() in Method

# Modify previous example so child calls parent method also.

#parent class
class Shape():
    def draw(self):
        print("draw a shape")

#child class
class Circle(Shape):
    def draw(self):
        super().draw()
        print("draw a circle") #this overrides the parent draw()

#object creation
c1=Circle()
c1.draw()