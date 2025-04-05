# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list.
#  The list is guaranteed to be non-empty, but there are no guarantees on its length.


def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    print(lst[-1])  # Using negative indexing to get the last element


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
        
    return lst


def main(): 
    lst = get_lst()  # Get the list from the user
    get_last_element(lst)  # Print the last element


if __name__ == '__main__':  # Correctly checking if this script is run directly
    main()
