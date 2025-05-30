# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, 
# and @price.deleter to delete it.



class Product:
    def __init__(self,  price):
        self._price = price

    @property
    def price(self):
        return self._price  # getter

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value  # setter
        else:
            raise ValueError("Price cannot be negative")
    

    @price.deleter
    def price(self):
        del self._price

p = Product(100)
print(p.price)
p.price = 200
print(p.price)
del p.price

# print(p.price)    # this will raise an error because the price attribute is deleted

