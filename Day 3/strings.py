name = "Ashim"
print(name)

description = """An innovative app designed to streamline daily tasks with ease, 
                 offering seamless integration and intuitive
                 user experience to enhance productivity and organization."""
print(description)

#finding the lenght of description

print(len(description))

first_name = "Ashim"
last_name = "Sapkota"
print(first_name,last_name)

#string are arrays => list

print(first_name[0])
print(first_name[len(first_name)-1])

# write a program to find the middle letters in the words
# the program must handle following conditions
# Eg: sudip = the result must be d
# eg: sudipe = the result must be di because the letter has even number of words 
#              and there is su in the first part and pe in last part

name2 = "sudip"
print(name2[len(name2)//2])

name1 = "sudipe"
print(name1[(len(name1)//2)-1]+name1[len(name1)//2])

name = input("Enter a name:")
if len(name)%2 == 1:
    print(name[len(name)//2])
else:
    print(name[(len(name)//2)-1]+name[len(name)//2])