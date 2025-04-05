# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    feet: float = float(input("Enter feet: "))
    inches: float = feet * 12
    print(str(feet) + " feet is " + str(inches) + " inches")

if __name__ == "__main__":
    main()
