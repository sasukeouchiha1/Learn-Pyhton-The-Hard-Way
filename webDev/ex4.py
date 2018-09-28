# initializes variable car to equal 100
cars = 100

# makes variable that tells how many seats are in a car
space_in_a_car = 4.0

# initializes variable drivers to equal 30
drivers = 30

# initializes variable passengers to 90
passengers = 90

# shows that the amount of cars minus the drivers equals cars that are not driven
cars_not_driven = cars - drivers

# shows that cars driven is equal to the amount of drivers
cars_driven = drivers

# shows that the capacity to carpool is equal to the space in the car multiplied by the cars driven
carpool_capacity = cars_driven * space_in_a_car

# average passangers is declared by the passengers divided by the cars driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars availible.")

print("There are only", drivers, "drivers availible.")

print("There will be", cars_not_driven, "empty cars today.")

print("We can transport", carpool_capacity, "people today.")

print("We have", passengers, "to carpool today.")

print("We need to put about", average_passengers_per_car, "in each car.")