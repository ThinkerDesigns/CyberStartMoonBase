# You've already seen how we can use strings.

# We can concatenate strings (join them up) like so:

firstString = "Hello, "
secondString = "World!"

print(firstString + secondString)

# But we can go further. We can use a format string.
# Look at this example:

count = "first"

print("Hello for the %s time." % (count))

# The %s is a format string specifier for a String.
# It tells Python that there is a string that needs to replace the %s.
# The string that replaces the %s comes after the %.

# There are other format string specifiers.
# Some of the ones you might need are:
# %s is for strings.
# %d is for integers. Think d is for digits.
# %f is for floats.

integer = 10

print("There are %d crates." % (integer))

floatpoint = 2.22

print("There are %f humans who understand code." % (floatpoint))

# You can also use multiple format string specifiers at once.

print("String: %s, Num: %d, Float: %f." % (count, integer, floatpoint))

# CHALLENGE 1: Save the integer 5 in the variable ch1_1, and
#              the string "robots" in the variable ch1_2
#              Use a format string to print the following sentence:
#              There are 5 robots in the room
