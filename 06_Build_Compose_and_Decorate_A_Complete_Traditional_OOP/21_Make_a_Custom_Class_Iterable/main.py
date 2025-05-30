# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object
#  iterable in a for-loop, counting down to 0.


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):           # __iter__() is called when the object is iterated over
        return self
    
    def __next__(self):          # __next__() is called to get the next item in the sequence
        if self.start <= 0:
            raise StopIteration      # Raises StopIteration when the sequence is exhausted
        value = self.start         # Stores the current value in the sequence
        self.start -= 1            # Decrements the current value
        return value               # Returns the current value



countdown = Countdown(0)
for num in countdown:
    print(num)