# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor.
#  Test it with callable() and by calling the object like a function.



class Multiplier:                  # __call__() is a special method that makes an object callable
    def __init__(self,factor):     # __init__() is a special method that initializes the object
        self.factor = factor       # self is the object itself and factor is the factor to multiply the input by

    def __call__(self, value):        # __call__() is a special method that makes an object callable
        return self.factor * value    # factor is the factor to multiply the input by
    



m = Multiplier(5)                      # create an instance of the Multiplier class
print(callable(m))                     # check if the object is callable
print(m(2))                            # print the result of the object being called with the value 2



