# import requests

# #change the userName to your name
# userName = "AkhilAayush"

# url = "https://cs-api.pltw.org/newuser/"

# response = requests.post(url+userName)

# #url is the web location that is storing and hosting the data.
# url = "https://cs-api.pltw.org/"

# #pString is the method used to post a string to an endpoint created with new user.
# pString = "string/?text="

# #A string without any spaces or special characters

# textToPost = 'hello world'
# response2 = requests.post(response.text+pString+textToPost)

# print(response2.text)


import requests

url = "https://cs-api.pltw.org/"

userName = "AkhilAayush"

# Construct the endpoint for the API request
pString = "string/?text="
textToPost = "Hello world"

# Send a POST request to the endpoint
response = requests.post(url + userName + "/" + pString + textToPost)

# Check the status code to ensure the request was successful
print("Status Code:", response.status_code)

# Print the headers of the response (may include useful information like content type, etc.)
print("Response Headers:", response.headers)

# Print the response text (this should be the data returned by the API)
print("Response Body:", response.text)

