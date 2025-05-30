# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, 
# add a subject field, and use super() to call the base class constructor.


# Solution:
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"
    
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"
    

# Example usage
if __name__ == "__main__":
    person = Person("Alice")
    teacher = Teacher("Bob", "Mathematics")

    print(person)  # Output: Person: Alice
    print(teacher)  # Output: Teacher: Bob, Subject: Mathematics