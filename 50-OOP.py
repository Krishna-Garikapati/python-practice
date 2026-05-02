# Class Variable vs Instance variable
# ❓ Question

# # Create a class variable school and instance variable name.

class Student:
    school = "NSCC"

    def __init__(self, name):
        self.name = name

s1 = Student("Krishna")
s2 = Student("Alex")

print(s1.school, s1.name)
print(s2.school, s2.name)