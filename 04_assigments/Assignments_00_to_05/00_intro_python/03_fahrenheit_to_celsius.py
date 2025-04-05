# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!



# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C



def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()      
