# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. 
# Apply it to a function say_hello().


def log_function_call(func):
    def wrapper(*args, **kwargs):         # *args and **kwargs are used to pass any number of arguments to the function
        print("Function is being called")  # this line is executed before the function is called
        return func(*args, **kwargs)      
    return wrapper

@log_function_call      # this line is used to apply the decorator to the function
def say_hello():          
    print("Hello, world!")


say_hello()

# Output:
# Function is being called
# Hello, world!

