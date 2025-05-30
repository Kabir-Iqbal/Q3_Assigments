# Assigment
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # public variable
        self._salary = salary  # protected variable
        self.__ssn = ssn  # private variable
        # The private variable is prefixed with double underscore to make it private
        # The protected variable is prefixed with single underscore to make it protected
        print("Employee object created with name:", self.name, 
              ", salary:", self._salary, ", ssn:", self.__ssn)
    def get_ssn(self):
        return self.__ssn
    def set_ssn(self, ssn):
        self.__ssn = ssn
    def get_salary(self):
        return self._salary
    def set_salary(self, salary):
        self._salary = salary
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
# Create an instance of the Employee class

employee = Employee("John Doe", 50000, "123-45-6789")

print("Public variable (name):", employee.get_name())


# Accessing the public variable
print("Public variable (name):", employee.name)
# Accessing the protected variable
print("Protected variable (_salary):", employee._salary)
# Accessing the private variable
try:
    print("Private variable (__ssn):", employee.__ssn)
except AttributeError as e:
    print("Error accessing private variable (__ssn):", e)
    
employee.set_ssn("987-65-4321")
print("Updated private variable (__ssn):", employee.get_ssn())
