from datetime import datetime

#function to greet user
def greet(username):
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = f"Good morning, {username}!"
    elif 12 <= hour < 17:
        greeting = f"Good afternoon, {username}!"
    else:
        greeting = f"Good evening, {username}!"
                        
    print( f"{greeting} It's great to see you!")

#get username as inut from user
user_input = input("Enter your name :")
username=user_input.capitalize()

#call greet function
greet(username)