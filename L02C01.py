# Programs aren't always static.
# Sometimes a program has to behave differently based on the
# information it gets. We can control the flow of a program
# using conditionals.

fun = 3
hacking = 5

if fun < hacking:
    print("Not enough fun!")

# Here we have an if statement.
# It says: if the value of fun is less than the value of hacking...
#          then print "Not enough fun!"

# Did you notice that there is a tab before print in our example?
# This is called a code block.
# The ':' after hacking means the start of the code block.
# And the tab at the start of every line after that means that code
# belongs to that block.

if fun < hacking:
    print("This code belongs to the if statement...")
    print("That's because there is a tab at the beginning.")
print("This code does not belong to the if statement.")
print("It will run no matter if the statement is true or not.")

# Let's prove it...

hacking = 2
fun = 10

if fun < hacking:
    print("Fun is not less than hacking, so this line will never print.")
print("But this line does not belong to the if statement.")
print("So it will print no matter what.")

# Here are the conditional operators you should know.
# You might recognise them from Maths class.

# < - Less than
# > - Greater than
# <= - Less than or equal to
# >= - Greater than or equal to
# == - Equals To

fun = 5
hacking = 5

if fun == hacking:
    print("The value of fun is equal to the value of hacking...")

# That's not all! We can also chain if statements together.

if fun < hacking:
    print("The value of fun is less than the value of hacking...")
elif fun > hacking:
    print("The value of hacking is greater than the value of fun...")
else:
    print("The value of hacking and the value of fun are equal...")

# In the above example we can see first we check if fun is less than
# hacking.
# If it is then it runs the code in the block that belongs to it.
# If it isn't, then we go on to the next if statement.

# The next statement checks if fun is greater than hacking.
# If it is then it runs the code in the block that belongs to it.
# If it isn't then it moves on to the last statement.

# The last statement is an 'else'. That just means if it didn't match
# any of the other if statements, then run the code in the block that
# belongs to it. Note that we also combine 'else' and 'if' into 'elif'.

# In this case, if it isn't greater than or less than then it must be
# equal to, it's the only thing left.
# You can have multiple 'elif's also.

people = 5
capacity = 50

# CHALLENGE 1: Check if the number of people is lower than the capacity.
#              If it is, print "success"
#              If the number of people is higher than the capacity,
#              print "too full"
#              If the number of people is equal to the capacity,
#              print "maximum people"

# CHALLENGE 2: Set the value of the people variable to 500.
#              Then run the same check from CHALLENGE 1 again.

# CHALLENGE 3; Set the value of the people variable to 50.
#              Then run the same check from CHALLENGE 1 again.
