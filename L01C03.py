# Now that you know the different data types, let's look at how to
# convert between them.

# To convert an integer to a string:
anInt = 4
aString = str(anInt)

# To convert a string to an integer:
aString = "20"
anInt = int(aString)

# To convert a string to a float:
aString = "3.333"
aFloat = float(aString)

# Here's an example...
carInfo = "Number of Doors: "
carDoors = "4"

# Now we can print the number of car doors with:

print(carInfo + carDoors)

# You can see that this prints out:
# Number of Doors: 4

# This works because both carInfo and carDoors are strings.
# Notice the quotation marks.

carDoors = 4

# Now carDoors is not a string anymore, it's an integer. (No quotation
# marks)
# If you tried to do:
# print(carInfo + carDoors)
# Then you would see an error:
# TypeError: cannot concatenate 'str' and 'int' objects.
# Try it for yourself.

carDoors = 2

# CHALLENGE 1: Convert carDoors to a string using type conversion.
# Save it in a new variable: carDoorsString

# CHALLENGE 2: Print out the number of doors in the car
# using print(carInfo + carDoorsString)
