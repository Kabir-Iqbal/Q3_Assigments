# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object 
# store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} works as a {self.position}."
    
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return [employee.get_info() for employee in self.employees]
    

# Example usage
dept = Department("Human Resources")
emp1 = Employee("Alice", "Recruiter")
emp2 = Employee("Bob", "HR Manager")
dept.add_employee(emp1)
dept.add_employee(emp2)
print(f"Employees in {dept.name} Department:")
for info in dept.list_employees():
    print(info)