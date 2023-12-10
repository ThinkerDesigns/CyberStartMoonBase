#
# Hide text in the image /tmp/image.gif
# Append the word alieneye to end of the file.
#
image_path = '/tmp/image.gif'
output_path = '/tmp/image.gif'

# Read the image file as binary
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()

# Text to be hidden in the image
hidden_text = "Hidden text: Hello, alieneye!"

# Encode the text as bytes
text_bytes = hidden_text.encode('utf-8')

# Append the text to the image data
image_data += text_bytes

# Append the word "alieneye" to the end of the file
image_data += b'alieneye'

# Write the modified data to a new file
with open(output_path, 'wb') as output_file:
    output_file.write(image_data)

print(f'Text hidden in the image and "alieneye" appended. Saved to {output_path}')
