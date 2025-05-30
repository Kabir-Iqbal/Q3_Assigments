# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    

# Example usage
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")  # Output: 25°C is 77.0°F