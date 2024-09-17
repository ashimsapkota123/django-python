#Assignment #1
#create a fizzbuzz game
#background : the players count from 1 to 100. it the number is divisible by 3 the player says fizz instead of the number 
#and if the number is divisible by 5 the play says buzz
#add if the number is divisible by both the number the player has to say "fizzbuzz"

for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


#Assignment #2
"""
create a random password generator
Ask if the length of the password 
include lower case,uppercase and symbols without function without input uppercase lowercase and digits to enter from user
"""
import random
import string

a = int(input("Enter a length of a password"))

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

passwords =[
    random.choice(lower_case),
    random.choice(upper_case),
    random.choice(digits),
    random.choice(symbols)
]

print(passwords)
all_character_password = (lower_case+upper_case+digits+symbols)


remaining_character = a -4
remaining_passwords = random.choice(all_character_password, k=remaining_character)
print(remaining_passwords)
print(remaining_character)

last_pass = passwords + remaining_character
random.shuffle(last_pass)
print("".join(last_pass))


