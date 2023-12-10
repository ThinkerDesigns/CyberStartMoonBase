# A function is just a bit of code that is taken out of the main
# program so it can be used over and over again.

# You've already been using functions. print() is a function.
# The print function takes in what you want to print as a parameter.
# Then it runs code that prints that to your screen.

# We're going to learn how to write our own functions.
# First we need to define a function with def:

def myfunction():
    print("This is my first function...")

# On it's own, this program doesn't do anything. We have to call the
# function first.

myfunction()

# Now this program should print "This is my first function..."

def myfunction(name):
    print("Hello " + name + ".")

# We've changed the function to take a parameter this time.
# Let's see how that works...

myfunction("Bob")

# Now this program will print "Hello Bob."

def myfunction(name):
    formatted = "Hello " + name + "."
    return formatted

# Now we've changed the function again. This time it doesn't print,
# it saves a string into the variable formatted. Then it returns the
# variable. By returning something, that just means you can save
# the output into a variable,

result = myfunction("Bob")

# Here we are returning "Hello Bob." and saving it into the variable
# 'result'. Let's check:

print(result)

# We can also take in multiple parameters:

def myfunction(name, age):
    return "I am " + name + " and I am " + str(age) + " years old."

# Now the function takes in a name and an age and returns the result.

result = myfunction("Bob", 26)

print(result)

# CHALLENGE 1: Write a function that takes in two integers and
#              multiplies them together then returns the result.

# CHALLENGE 2: Run the function from CHALLENGE 1, passing in the
#              integers 99 and 52 and print the result.

# CHALLENGE 3: Write a function that takes two integers and prints
#              the string "I am X ft Y inches tall", replacing the
#              X and Y with the numbers passed into the function.

# CHALLENGE 4: Run the function from CHALLENGE 3, passing in 6 and 2
#              as the parameters.

# You should end up with 2 lines output from these 4 challenges.
