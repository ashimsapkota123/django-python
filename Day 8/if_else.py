age = int(input("Enter your age: "))
if 18<=age<40:
    sex = input("Enter M for male and F for female:")
    numbers_of_days = int(input("Numbers of days: "))
    if 18<=age<30:
        if sex == "M":
            print(numbers_of_days*700)
        elif sex == "F":
            print(numbers_of_days*750)
    elif 30<=age<40:
        if sex == "M":
            print(numbers_of_days*800)  
        elif sex == "F":
            print(numbers_of_days*850)
else:
    print("Enter appropriate age")



dict = {40:"Ashim"}
print(dict)