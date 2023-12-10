# An array is just a collection of data.
# Let's look at an example:

myarray = ["Hello", "World!", 28, 22.5]
print(myarray) # This prints all the values in the array.
print(myarray[0]) # This prints the first value in the array
# (We start counting from 0)
print(myarray[1]) # This prints the second value in the array.
print(myarray[2]) # This prints the third value in the array.
print(myarray[3]) # This prints the fourth value in the array.

# We can see we can access positions in the array using square
# brackets [].You can also add to an array...

myarray.append("morestuff")
print(myarray) # We can see "morestuff" got added to the end
# of the array.

# We can also change the values in a specific position of the array:

myarray[3] = "changed"
print(myarray) # We can see the fourth value in the array was
# changed to "changed".

# We can also remove from the array:

myarray.pop(3) # This removes the fourth item from the array
print(myarray)

# Similar to arrays are dicts or dictionaries.
# With arrays, you can only reference positions in the array using
# numbers.
# With a dict, you associate one value with another, a key-value pair.
# The colon ':' differentiates the key from the value.
# In the example below, name is a key. Bob is the value associated with name.

mydict = {"name": "Bob", "age": 23, "height": 180}

# In this example, name is the key and Bob is the value. If you
# want to find out the name you can just do:

print(mydict["name"])

# To get the age:

print(mydict["age"])

# CHALLENGE 1: Create an array with the following values in it in
#             order:
#             42, 1337, "Coffee", "Anonymous" then print the array.

# CHALLENGE 2: Add two more values to the end of the array you created
#              in CHALLENGE 1: "Blue", "Sky" then print the array.

# CHALLENGE 3: Print the fourth value in the array you created in
#              CHALLENGE 1.

# CHALLENGE 4: Create a dict that includes the following values in
#              order: "Subject": "Hacking", "Grade": "A".

# CHALLENGE 5: Print the grade value in the dictionary you created in
#              CHALLENGE 4.
