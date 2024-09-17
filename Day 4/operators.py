# logical operators
# and, or, not

#write a program to compare three number and find the greatest among them

num1 = 10
num2 = 15
num3 = 12
if num1>num2 and num1>num3:
    print("num1 is the greatest.")
elif num1<num2>num3:
    print("num2 is the greatest.")
elif num1<num3>num2:
    print("num3 is the greatest.")
else:
    print("The numbers are equals.")

#wap to decide whether you can join the party
#condition: you have to be relative or above 18 years

age = 19
relative = False

if age>=18  or relative:
    print("You can join the party.")
else:
    print("You can't join the party.")

#membership operators
# in, not in

a = "Pokhara"

if "P" in a:
    print("ok is present")
else:
    print("ok is not present")

