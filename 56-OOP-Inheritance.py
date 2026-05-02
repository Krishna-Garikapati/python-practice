# If Two Parent Classes Have Same Method Name

# 👉 Python uses something called Method Resolution Order (MRO)
# → It decides which method runs first

# 📌 Rule (Simple)

# 👉 Python checks left to right (order of inheritance)
# Python uses C3 Linearization (MRO algorithm) internally

class A:
    def show(self):
        print("From A")

class B:
    def show(self):
        print("From B")

class C(A, B):# Because A comes before B
    pass

obj = C()
obj.show() #Output: From A. 



#vice versa if class C(B,A) then output is From B