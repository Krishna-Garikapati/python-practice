class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # ✅ Instance method (updates object)
    def apply_bonus(self, bonus):
        new_salary = Employee.calculate_bonus(self.salary, bonus)
        self.salary = new_salary
        print(f"{self.name}'s new salary: ${self.salary}")

    # ✅ Static method (calculation only)
    @staticmethod
    def calculate_bonus(salary, bonus):
        return salary + bonus


# Create object
e1 = Employee("Krishna", 5000)

# Apply bonus
e1.apply_bonus(1000)