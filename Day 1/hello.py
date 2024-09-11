from datetime import datetime

def greet_based_on_time():
    now = datetime.now()
    
    current_hour = now.hour

    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    print(greeting)

greet_based_on_time()
