# Write a function that takes a list of numbers and returns the sum of those numbers.


def add_many_numbers(numbers)-> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()