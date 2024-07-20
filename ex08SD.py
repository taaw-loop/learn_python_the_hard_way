formatter = "{} {} {} {}" # Setting up the string to be used as format.

print(formatter.format(1, 2, 3, 4,)) # This prints out the .format text in the formatter string context.
print(formatter.format("one", "two", "three", "four")) # ""
print(formatter.format(True, False, False, True)) # ""
print(formatter.format(formatter, formatter, formatter, formatter)) # ""
print(formatter.format(
    "Your abhorrent stench of turning flesh lingers",
    "Peregrine ponderings tightening the tether",
    "Succor sepulchered epochs ago",
    "Barring sheer abandonment"
)) # ""
