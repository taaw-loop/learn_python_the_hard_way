# When "cars" is typed, it's interpreted as 100.
cars = 100 
# When "space_in_a_car" is typed, it's interpreted as 4.0.
space_in_a_car = 4.0
# When "drivers" is typed, it's interpreted as 30. 
drivers = 30 
# When "passenger" is typed, it's interpreted as 90.
passengers = 90
# When "cars_not_driven" is typed, it's interpreted as 100 - 30 (cars - drivers). 
cars_not_driven = cars - drivers
# When "cars_driven" is typed, it is interpreted as 30 (drivers). 
cars_driven = drivers
# When "carpool_capacity)" is typed, it's interpreted as 30 * 4.0 (cars_driven * space_in_a_car). 
carpool_capacity = cars_driven * space_in_a_car
# When "average_passengers_per_car" is typed, it's interpreted as 30 / 90 (passengers / cars_driven)
average_passengers_per_car = passengers / cars_driven 

# The words in "" are printed and the word "cars" is displayed as 100 because of the set variable.
print("There are", cars, "cars available.") 
# The words in "" are printed and "drivers" is displayed as 30 because of the set variable.
print("There are only", drivers, "drivers available.") 
# The words in "" are printed and "cars_not_driven" is displayed as 70 because of the set variable (cars - drivers).
print("There will be", cars_not_driven, "empty cars today") 
# The words in "" are printed and "carpool_capacity" is displayed as 120.0 because of the set variable (cars_driven * space_in_a_car).
print("We can transport", carpool_capacity, "people today.")
# The words in "" are printed and "passengers" is displayed as 90 because of the set variable. 
print("We have", passengers, "to carpool today.")
# The words in "" are printed and "average_passengers_per_car" is displayed as 3.0 because of the set variable (passengers / cars_driven). 
print("We need to put about", average_passengers_per_car, 
      "in each car.") 

# This may mean that it's looking back at the most resent error/bug thrown
# (Traceback (most recent call last):
# The most recent error/bug being something on line 8
#  File "ex4.py", line 8, in <module>
# showing line 8
#    average_passengers_per_car = car_pool_capacity / passenger
# The NameError meaning that the variable "car_pool_capacoty" should match the set variable "carpool_capacity"
#NameError: name 'car_pool_capacity' is not defined 
 