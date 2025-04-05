# There are times where you are working with lots of different data within a function that you want to return. While generally, we want 
# to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.



def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email


def main():
    first_name, last_name, email = get_user_data()
    print(f"Received the following user data: ({first_name}, {last_name}, {email})")

if __name__ == "__main__":
    main()

