# Create a class Logger that prints a message when an object is created (constructor) 
# and another message when it is destroyed (destructor).



class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} destroyed")



logger1 = Logger("Ahmed")






