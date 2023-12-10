#
# Find the file in the alien directories in /tmp/aliendir to get the flag
#
import os

def find_files(directory):
  """
  Searches for files in a directory and its subdirectories.

  Args:
    directory: Path to the directory to search.

  Yields:
    Full path of each file found.
  """
  for path, _, files in os.walk(directory):
    for filename in files:
      full_path = os.path.join(path, filename)
      yield full_path

# Set the directory to search
alien_dir = "/tmp/aliendir"

# Find all files in the alien directory and its subdirectories
for file_path in find_files(alien_dir):
  print(f"Found file: {file_path}")
