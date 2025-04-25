from datetime import datetime
import random

#function to greet user
def greet(user_name):
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = f"Good morning, {user_name}!"
    elif 12 <= hour < 17:
        greeting = f"Good afternoon, {user_name}!"
    else:
        greeting = f"Good evening, {user_name}!"

    greetings_list = [
    f"{greeting} It's great to see you!"
    f"{greeting} Nice to meet you.",
    f"{greeting} Hope you're having a great day.",
    f"{greeting} It's a pleasure to see you.",
    f"Good day, {user_name}! Hope you're doing well.",
    f"Hey there, {user_name}! Nice to meet you."]

    unique_greet = random.choice(greetings_list)

    print(unique_greet)

#get username as inut from user
user_input = input("Enter your name :")
username=user_input.capitalize()

#call greet function
greet(username)