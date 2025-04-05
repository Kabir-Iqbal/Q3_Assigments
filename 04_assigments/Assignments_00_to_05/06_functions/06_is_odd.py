# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd


def is_odd(num: int):
    return num % 2 == 1

# There is no need to edit code beyond this point

def main():
    num = int(input("Enter a number: "))
    if is_odd(num):
        print(f"{num} odd")
    else:
        print(f"{num} even")

if __name__ == "__main__":
    main()
