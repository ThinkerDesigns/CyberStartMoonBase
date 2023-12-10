#
# Find the valid png file in the /tmp directory using magic bytes.
# The code is hidden in this file.
#
import os

# Define the PNG magic bytes
png_magic_bytes = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"

def is_valid_png(data):
  """
  Checks if the provided data starts with the PNG magic bytes.

  Args:
    data: Bytes of the file to check.

  Returns:
    True if the data is a valid PNG, False otherwise.
  """
  return data.startswith(png_magic_bytes)

def find_valid_png(directory):
  """
  Searches for a valid PNG file in the provided directory.

  Args:
    directory: Path to the directory to search.

  Returns:
    Full path of the valid PNG file or None if no valid PNG is found.
  """
  for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
      with open(file_path, "rb") as f:
        data = f.read(len(png_magic_bytes))
        if is_valid_png(data):
          return file_path
  return None

# Search for valid PNG file in /tmp directory
valid_png_path = find_valid_png("/tmp")

# Check if a valid PNG was found
if valid_png_path:
  # Open the valid PNG file and display its contents
  with open(valid_png_path, "rb") as f:
    data = f.read()
    print(data)
else:
  print("No valid PNG file found in /tmp")
