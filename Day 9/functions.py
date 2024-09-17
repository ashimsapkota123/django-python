#without using function
#write a program to print the following lines
#1 . I am ashim
#2 . I am Sudip
#3 . I am Shraddha
print("I am ashim")
print("I am Sudip")
print("I am Shraddha")



#with using function
def print_name(name1,name2,name3=None):#passing parameter in print_name
    print("I am " + name1)
    print("I am " + name2)
    print("I am " + name3)

print_name("Ashim","Sudip","Shraddha")#passing arguments in print_name
print_name("Hari","Shyam","Ram")

def print_name(name1,name2,name3=None):#passing parameter in print_name
    print("I am " + name1)
    print("I am " + name2)
    if name3 != None:
        print("I am " + name3)

print_name("Ashim","Sudip","Shraddha")#passing arguments in print_name
print_name("Hari","Shyam")

def print_name(*names):
    for name in range(len(names)):
        print("I am " + names[name])
print_name()
    