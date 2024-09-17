#slicing strings

a = "Prime Learning, Palikhe Chowk"

print(a[::-1])

if "Prime" in a:
    print("Prime is present in the string")
else:
    print("Prime is not present in the string")


print(a.capitalize())
print(a.upper())
print(a.lower())

b = a.lower()
c = a.upper()
d = a.capitalize()
print(b)
print(c)
print(d)

print(a)

print(a.strip())

r = a.replace("a","b")
print(r)

words = a.split(" ")
print(words)
print(len(words))

print("The words a is: ",words.count("P"))


#store your first name last name and address in three variables and print like 
#My name is John Doe and I live in Pokhara

first_name = "Ashim"
last_name = "Sapkota"
address = "Pokhara"
print("My name is",first_name,last_name,"and I live in",address)


text = "We are so called \"Pokharelis\""
print(text)
first_name = "Ashim Ashim Sapkota"
print(first_name.center(100))
print(first_name.casefold().center(100))
print(first_name.count("Ashim"))
print(first_name.encode())
print(first_name.find("Sapkota"))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#assignment
'''write a program to reverse a string and print it to be palindrome if the original string and reversed string are same 
without using built in functions'''

name = input("Enter a word to check the word is palindrome or not: ")
reverse_word = ""
name = name.lower()  
for i in range(len(name)):
    reverse_word = name[i] + reverse_word

if reverse_word == name:
    print("Palindrome")
else:
    print("Not a palindrome") 
    