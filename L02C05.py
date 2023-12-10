# In programming, there are many situations where we have to repeat a
# task over and over until a condition is met. We use loops for this.

# The first type of loop we will look at is a while loop.
# Like the name suggests, a while loop will keep repeating while a
# condition is true.

count = 0
while count < 10:
    print("The count is: " + str(count))
    count = count + 1

# In our example, the condition is that count should always be
# less than 10.
# When count is more than 10, the loop will stop executing.
# Our example will print "The count is 0" then "The count is 1" and
# so on until "The count is 9"

hungryPeople = 8
pizza = 10

while hungryPeople > 0:
    pizza -= 1
    hungryPeople -= 1
    print("Someone ate a pizza.")
print("There are no more hungry people")

# In this second example we are using pizza -= 1 instead of
# pizza = pizza - 1.
# It's the same thing, it's just a short way of writing it.
# You can use the same shortcut for addition.
# For example pizza += 1 is the same as pizza = pizza + 1
# You will see when the loop exits that
# "There are no more hungry people" will print.
# That is because hungryPeople > 0 is no longer true so the
# code moves on to line 24.

# It's very important that you make sure the condition where a loop
# exits will always be met. If it doesn't get met, you will have an
# infinite loop. If you have an infinite loop, the program will never
# stop running unless you force it to quit.

# The other type of loop is a for loop. For loops are particularly
# useful for going through arrays. Let's look at an example:

myarray = ["Strong", "Coffee", "Is", "The", "Best"]

for x in myarray:
    print(x)

# This is the most basic form of a for loop. Here, each time the loop
# executes, x will be the next value in the array. The loop will exit
# on it's own when there are no more array values.

# So for example, the first time the loop runs, x will be "Strong",
# the second time x will be "Coffee" and so on...

# We can also do ranges in for loops.
# This will print 0 through to 49.
for x in range(0, 50):
    print(x)

# CHALLENGE 1: Create an empty array called numbers.
numbers = []

# CHALLENGE 2: Write a while loop that will add 100 numbers to the
#              array, starting from the number 100 and incrementing by
#              2 each time. For example, start from 100, then the next
#              number added will be 102, then 104 and so on.
count = 100
while count <= 300:
  numbers.append(count)
  count = count + 2

# CHALLENGE 3: Write a for loop that will look through your numbers
#              array and print out each value in the array.
for x in numbers:
  print(x)
