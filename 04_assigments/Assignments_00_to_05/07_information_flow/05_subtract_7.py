# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper 
# function! If you're stuck, revisit the add_five example from lecture.



def subtract_seven(num: int):
    return num - 7


def main():
    num = int(input("Enter a number: "))
    print(subtract_seven(num))  

if __name__ == "__main__":
    main()
