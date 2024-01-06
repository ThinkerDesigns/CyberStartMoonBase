#
# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout. If this occurs try narrowing
# down your search
#
import urllib.parse
import urllib.request

url = "http://127.0.0.1:8082"
startingKey = 5500
endingKey = 5600
hdr = {}

while startingKey <= endingKey:
    hdr = { 'x-api-key' : str(startingKey) }
    req = urllib.request.Request(url, headers=hdr)
    response = urllib.request.urlopen(req)
    print(response.read())
    startingKey = startingKey + 1
