# You can't really understand conditionals without understanding logic.
# Computers are binary, they think in 1s and 0s. Or put another way,
# True or False.
# If a 1 is a True, then a 0 is a False.

# Logic is Maths. So it's not surprising that calculating logic looks
# a lot like solving Maths problems.
# True AND False = False
# It looks very similar to:
# 1 + 3 = 4

# There are several logical operators which you should know:
# and - Logical AND. Both sides of the equation have to be True for it
# to be True. If not it's False.
# or - Logical OR. If either side of the equation is True then it's
# True. If not it's False.
# not - Logical NOT. Turns a True result into False and a False into
# a True.

print(True and True) # This prints 'True'
print(True and False) # This prints 'False'
print(True or False) # This prints 'True'
print(False and True) # This prints 'False'
print(False and False) # This prints 'False'
print(False or False) # This prints 'False'

# This prints 'False', because the 'not' reverses it.
print(not(True and True))
# This prints 'True', because the 'not' reverses it.
print(not(False and False))

# Did you notice how every time we open a bracket '(' we have to close it ')'?
# This is called bracket matching. If you leave open brackets that
# never get closed, you will start seeing errors.

# You can also see how this works in conditionals. Let's use our
# example from the previous challenge.

fun = 2
hacking = 6

if hacking > fun:
    print("more hacking")

# hacking > fun is the key here. What does hacking > fun come out to?
print(hacking > fun) # This prints 'True'.

# So actually what is happening here is we're saying if something
# is true, then continue into the code block.
# What happens if we negate it with not?

print(not(hacking > fun)) # This prints 'False'

# So if we used that in a conditional?

if not(hacking > fun):
    print("This isn't going to run...")

# How about checking for two things in one if statement?

pizza = 4

if (hacking > fun) and (pizza > fun):
    print("more hacking and more pizza...")

# Here, hacking > fun is True. pizza > fun is also True.
# True and True = True, so the if statement is True.

if (hacking < fun) or (pizza > fun):
    print("at least there's pizza.")

# Here hacking < fun = False. pizza > fun is True.
# So it ends up being: False or True, which equals True.

# CHALLENGE 1: Print the result of true or true.

# CHALLENGE 2: Print the result of true or false.

# CHALLENGE 3: Print the result of false or true.

# CHALLENGE 4: Print the result of false or false.

# CHALLENGE 5: Use not to negate the result of true OR false and
# print the result.
