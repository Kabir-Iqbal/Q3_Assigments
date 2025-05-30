# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.



class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting")




# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print(my_car.brand)

# Access public method
my_car.start()