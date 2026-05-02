# 🔹 5. str Method 🔥
# ❓ Question

# Override __str__ so printing object shows details.

class Student:
    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    #method
    def __str__(self):
        return f"{self.name,{self.age}}"

    #object creation
s1=Student("Krishna",29)
s2=Student("Surya",29)
print(s1,s2)