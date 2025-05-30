# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car
#  class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP started."
    
class Car():
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start(self):
        return f"{self.make} {self.model} - {self.engine.start()}"


# Example usage
engine = Engine(150)    
car = Car("Toyota", "Corolla", engine)
print(car.start())  # Output: Toyota Corolla - Engine with 150 HP started.
# Output: Toyota Corolla - Engine with 150 HP started.
