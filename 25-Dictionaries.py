# Q1. Create & Access Dictionary
# 👉 Create a dictionary for a student and print the name.

student = {
    "name":"krishna",
    "age":29,
    "Address":"xxxx",
    "class":"IT Programming",
    "Year":"2026"
}

print(student["name"])

# Q2. Print All Keys, Values, Items
print(student.keys())
print(student.values())
print(student.items())

# Q3. Add new value
student["department"]="IT"
print(student)

#Q4.Update existing value
student["age"]=28
print(student)