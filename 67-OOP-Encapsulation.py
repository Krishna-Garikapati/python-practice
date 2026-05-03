# Q2 — Add Setter with Validation

# 👉 Question
# Add a setter to ensure name is not empty.

class Person:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        if name:
            self.__name=name


#     but i already set value in init then why again in setter
#     Short answer
# __init__ → sets the initial value
# set_name() → controls future updates

#object
p1=Person("Krishna")
print(p1.get_name())
