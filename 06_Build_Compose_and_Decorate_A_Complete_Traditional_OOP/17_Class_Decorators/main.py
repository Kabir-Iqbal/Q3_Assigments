# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!".
#  Apply it to a class Person.


def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass


p = Person()
print(p.greet())


# Output:
# Hello from Decorator!
