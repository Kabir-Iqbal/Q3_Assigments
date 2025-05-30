# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception 
# if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is less than 18")     # Raises the custom exception
    else:
        print("Age is greater than 18")


check_age(17)    # Raises the custom exception
check_age(19)    # Does not raise the custom exception
