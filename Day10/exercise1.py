"""
create a student report based on subjects(args) and additional information (kwargs).
print the information in keyword args and find the print the subjects in args
"""

# def subjects(*subject, **information):
#     print(subject,information)
# subjects("Math","Nepali","English","Science",name = "Ashim",age = 19,address = "Syangja")

# #other way
# def subjects(*subjects):
#     print(subjects)
# subjects("Math","Nepali","English","Science")

# def information(**info):
#     print(info)
# information(Name="Ashim Sapkota",Address = "Syangja",Age = 19)

#create a function that accepts a list of fruits as a arguments and print the fruits in the list

def fruits(*fruits):
    print(list(fruits))
fruits("apple","banana","cherry","mango","orange")

def fruit(*fruit):
    return list(fruit)
print(fruit("apple","banana","cherry","mango","orange"))

