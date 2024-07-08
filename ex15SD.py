from sys import argv #I mport argv from the sys module

script, filename = argv # Getting command line arguments (when running the file) and assigning it 2 variables.

txt = open(filename) # Open the file using the file name (from begging cmd line arguments).

print(f"Here's your file {filename}:") # Print out the file name and print the contents of the opened file using read.
print(txt.read())

print("Type the filename again:") # Print out instructions and ask user input using input.
file_again = input("> ")

txt_again = open(file_again) # Open the file using the file name and assignging it to a variable.

print(txt_again.read()) #  Print out the file name and print the contents of the opened file using read.
