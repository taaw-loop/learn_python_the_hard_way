# types_of_people is the variable and it = 10.
types_of_people = 10
# x is = to the string within the "" and f is formating the string inside of that which is types_of_peopls, which = 10.
x = f"There are {types_of_people} types of people"

# Setting the variable name binary to = "binary"
binary = "binary" 
# Setting the variable name do_not to = "don't"
do_not = "don't" 
# y is = to the string within the "" and f is formating the string inside of that which is binary, which = binary, and do_not, which = don't.
y = f"Those who know {binary} and those who {do_not}."

# Print's the string and inner string of x.
print(x)
# Print's the string and inner string of y.
print(y)


print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)