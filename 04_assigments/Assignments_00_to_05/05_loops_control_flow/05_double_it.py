# Write a program that asks a user to enter a number. Your program will then double that number and print out the result.
#  It will repeat that process until the value is 100 or greater.


user_input : int = int(input("Enter a number: "))



# Keep doubling the number until it's 100 or greater
while user_input < 100:
    user_input *= 2  # Double the number
    if user_input >= 100:
        break
    print(user_input)







