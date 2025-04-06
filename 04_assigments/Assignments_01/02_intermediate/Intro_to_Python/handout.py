# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard 
# a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of 
# its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!



# Gravitational constants for planets
mercury: float = 37.6
venus: float = 88.9
mars: float = 37.8
jupiter: float = 236.0
saturn: float = 108.1
uranus: float = 81.5
neptune: float = 114.0

# Ask the user for their weight on Earth
earth_weight = float(input("Enter your weight on Earth (kg): "))

# Prompt the user for the name of a planet
planet = input("Enter a planet: ").lower()  # .lower() handles case sensitivity

# Determine the gravitational constant for the selected planet
if planet == "mercury":
    gravity_constant = mercury
elif planet == "venus":
    gravity_constant = venus
elif planet == "mars":
    gravity_constant = mars
elif planet == "jupiter":
    gravity_constant = jupiter
elif planet == "saturn":
    gravity_constant = saturn
elif planet == "uranus":
    gravity_constant = uranus
else:
    gravity_constant = neptune

# Calculate the equivalent weight on the selected planet
planetary_weight = earth_weight * gravity_constant / 100
rounded_planetary_weight = round(planetary_weight, 2)

# Print the result
print("The equivalent weight on " + planet.title() + " is: " + str(rounded_planetary_weight) + " kg")
