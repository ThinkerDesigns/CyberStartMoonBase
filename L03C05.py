import re

html = """
<html>
<head>
    <title>Regex Demo</title>
</head>
<body>
    <div class='firstDiv'>Hello</div>
    <div class='secondDiv'>Hello</div>
</body>
</html>
"""

# CHALLENGE 1: Write a regex search that extracts all the classes from
#             the divs and saves them into an array.

pattern = "class='(.*)'"
data = re.findall(pattern, html)

# CHALLENGE 2: Write a loop that goes through the array from
#              CHALLENGE 1 and prints the contents.

for x in data:
    print(x)

# Click "Back to my code" below to restore your code
# or
# Click "Submit code" above to get the flag
