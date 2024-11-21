
# Creating the endpoint
#  import requests

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







# #Post Request
# import requests

# url = "https://cs-api.pltw.org/AkMuthy"
# pString = "?text="
# textToPost = "Hello"
# response = requests.post(url + pString + textToPost)
# print(response.text)
# print(response.status_code)


# print(url + pString + textToPost)



# #Get Request
# import requests

# url = "https://cs-api.pltw.org/"

# userName = "AkMuthy"

# response = requests.get(url + userName)
# print(response.status_code)
# print(response.headers)
# print(response.text)

# #Increment code
# import requests

# url = "https://cs-api.pltw.org/AkMuthy/increment?id="
# num = str(2)

# for _ in range(3):
#     response = requests.post(url+num)

# print(response.status_code)
# print(response.headers)
# print(response.text)


# # Interview Post

import requests
global url
API = "https://cs-api.pltw.org/"
user = input("Which user would you like to hack:")


url = API + user


def INC():
    id = "increment?id"


    num  = input("What index would you like to change:")
    count = input("what number would you like to change it to:")


    for _ in range (count):
        inc_response = requests.post(url+id+num)


    print(inc_response.status_code)
    print(inc_response.headers)
    print(inc_response.text)


def POST():
    pString = "?text="
    my_text = input("What do you want to post:")
    post_response = requests.post(url+pString+my_text)


    print(post_response.status_code)
    print(post_response.headers)
    print(post_response.text)


for n in range(10):
    POST()

    







