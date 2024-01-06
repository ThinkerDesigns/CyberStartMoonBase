#
# Write a script to generate a passphrase by taking words from
# /tmp/words.txt
# The wordNumbers array holds three random numbers. Each number
# corresponds to a word in words.txt. So for example
# wordNumbers[1] is the second word in /tmp/words.txt.
# Put a space between each word and print it out
#


with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()

wordNumbers = data.rstrip().split("\n")
a = int(wordNumbers[0])
b = int(wordNumbers[1])
c = int(wordNumbers[2])
heybuddy = []
with open("/tmp/words.txt", "r") as file:
  for line in file:
    stripped_line = line.strip()
    line_list = stripped_line.strip()
    heybuddy.append(line_list)  
  print(heybuddy[a], heybuddy[b], heybuddy[c])
