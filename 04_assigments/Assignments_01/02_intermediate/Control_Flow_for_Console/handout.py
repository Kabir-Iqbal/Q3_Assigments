# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop
#  a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent.
#  You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's),
#  you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.



import random

num_rounds = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: keep track of your score
    your_score = 0
    computer_score = 0

    for i in range(num_rounds):
        print(f"Round {i+1}:")
        your_number = random.randint(1, 100)
        print("Your number is:", your_number )

        computer_number = random.randint(1, 100)
        # Milestone 2: Get user input for their choice
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        # Extension 1: Make sure the player inputs a valid choice (higher or lower)
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ")

        if choice == "higher" and your_number > computer_number:
            your_score += 1
            print("You were right! The computer's number was", computer_number)
        elif choice == "lower" and your_number < computer_number:
            your_score += 1
            print("You were right! The computer's number was", computer_number)
        else:
            print("Aww, that's incorrect. The computer's number was", computer_number)
        # Milestone 5: keep track of your score
        print("Your score is now", your_score)
        print()



    # Extension 2: Conditional ending messages based on performance
    print("Your final score is", your_score)

    if your_score == num_rounds:
        print("Wow! You played perfectly!")
    elif your_score > num_rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
