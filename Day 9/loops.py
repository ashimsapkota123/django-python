#two different types of loops 
#1. for loop
#2. while loop

#while loop
i = 0
while i <= 5:
    if  i != 3:
       print(i)
    i += 1
print(f"""

++++++++++++++++++++++++++++++++++++++++++++++++++++++++
========================================================
--------------------------------------------------------
      
    """)

ip_address = ["192.168.1.1","192.168.1.0","192.168.1.2","192.168.1.3","0.0.0.0","78.45.256.256"]

"""
Write a program to evaluate the above ip and break the executation if the request is from 0.0.0.0 using for loop

"""
ip_address1 = len(ip_address)
for i in range(ip_address1):
    if ip_address[i] == "0.0.0.0":
        break
    else:
        print(ip_address[i])

i = 0 #reinitialize the value of i to set to 0
while i<len(ip_address):
    if ip_address[i] == "0.0.0.0":
        break
    else:
        print(ip_address[i])
    i +=1

#finding the common between two array using for loops

fruits1 = ["redberry","jackfruit","orange","cherry","guava","apple"]
fruits2 = ["apple","banana","cherry"]

for i in range(len(fruits1)):
    for j in range(len(fruits2)):
        if fruits1[i] == fruits2[j]:
            print(fruits2[j])

for fruit in fruits1:
    if fruit in fruits2:
        print(fruit)