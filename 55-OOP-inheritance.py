# Q4. Method Overriding

# Create class Shape with method draw().
# Override it in class Circle.
#child can override parent method
#parent class
class Shape():
    def draw(self):
        print("draw a shape")

#child class
class Circle(Shape):
    def draw(self):
        print("draw a circle") #this overrides the parent draw()

#object creation
c1=Circle()
c1.draw()

