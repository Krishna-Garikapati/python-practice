# Q4 — Operator Overloading

# 👉 Question

# Create a class Number with attribute value.
# Overload + to add two objects.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

n1 = Number(10)
n2 = Number(20)

result = n1 + n2
print(result.value)   # 30