from sys import argv
# read the WYSS section for how to run this
script, first, second, third, fourth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

user_input = input("Add some text here: ")
print(f"Your input was: {user_input}.")

# run script in terminal as: python3 ex13SD.py first 2nd 3rd 4th
