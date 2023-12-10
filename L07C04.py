#
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#
import re

def extract_flag(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # Use regular expression to extract alphanumeric characters
        alphanumeric_characters = re.findall(r'[a-zA-Z0-9]+', file_contents)

        # Join the alphanumeric characters to form a potential flag
        potential_flag = ''.join(alphanumeric_characters)

        return potential_flag

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Path to the intercepted file
file_path = '/tmp/destroymoonbase.gif'

# Extract potential flag from the file
flag = extract_flag(file_path)

# Print the potential flag
if flag:
    print(f"Potential flag: {flag}")
else:
    print("Failed to extract the potential flag.")
