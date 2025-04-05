# Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function 
# to retrieve your name and then prints it in a greeting.

# Here's a sample run of the program where the name we've decided to return is Sophia (the autograder expects the returned name to be 
# Sophia):

# Howdy Sophia ! 🤠


def get_name():
    return "Sophia"

# There is no need to edit code beyond this point

def main():
    name = get_name()
    print(f"Howdy {name} ! 🤠")

if __name__ == "__main__":
    main()
