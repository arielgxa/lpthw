# Total number of cars
cars = 100

# Space for passengers in a car
# space_in_a_car = 4.0
space_in_a_car = 4

# Number of drivers
drivers = 30

# Total number of passengers to transport
passengers = 90

# Number of cars withou drivers
cars_not_driven = cars - drivers

# Number of cars with drivers
cars_driven = drivers

# Number of passengers that can be transported based on number of available cars
# and capacity
carpool_capacity = cars_driven * space_in_a_car

# Average number of passengers in each car
average_passengers_per_car = passengers / cars_driven


# Print available cars
print "There are", cars, "cars available."

# Print available drivers
print "There are only", drivers, "drivers available."

# Print empty cars
print "There will be", cars_not_driven, "empty cars today."

# Print number of passengers transportable
print "We can transport", carpool_capacity, "people today."

# Print number of passengers needing transport
print "We have", passengers, "to carpool today."

# Print average number of passengers per car
print "We need to put about", average_passengers_per_car, "in each car."


# STUDY DRILL: There was an error as the variable declared in line 7 was named
# carpool_capacity, and the variable car_pool_capacity had not been defined.
