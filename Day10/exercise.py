#write a function to accept two numbers and return additon and substraction of them 
def add_sub(num1,num2):
    return num1+num2,num1-num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(add_sub(num1,num2))


#keyword arguments 
def add_sub(num1,num2):
    return num1+num2,num1-num2

x = add_sub(num2=6,num1=5)
print(x)

def print_name(**names):
    print("My name is: ",names)

print_name(names1 = "Ashim",names2= "Ram",names3 = "Shyam")

def print_name(**names):
    print(names["names1"])

print_name(names1 = "Ashim",names2= "Ram",names3 = "Shyam")



