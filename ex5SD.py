name = 'Thomas A. Anderson'
age = 29 # maybe a fib
height = 69 * 2.54 # inches to centimeters
weight = 190 * 0.453 # lbs to kg
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

# The f function is formating the {} variables
print(f"Let's talk about {name}.")
print(f"He's around {age} years of age.")
# The round() function is rounding up the floating point number.
print(f"He's {round(height)} centimeters tall.")
print(f"He's {round(weight)} kilograms heavy.")
print("Actually that's not too crazy heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usally {teeth} depending on the animal flesh.")

# this line is tricky, try to get it exactly right
# The variables are being use to calculate the total.
total = age + height + weight
print(f"If I add {age}, {round(height)}, and {round(weight)} I get {round(total)}.")
