# Q8. Multilevel Inheritance

# Create 3 classes A → B → C.
# Add method in A and call from C.

class A():
    def display(self):
        print("multilevel inheritance")
class B(A):
    pass
class C(B):
    pass

#object creation for class C
c1=C()
c1.display()