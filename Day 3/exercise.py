#revision exerice
"""
    Write a python script that does the following:

    Create a list of 5 different types of data: an integer, a float, a string, a boolean, and a list.
    print the type of each element in the list using the type() function.
    Add a dictionary to the list that contains keys of different types and values of different types.
    Print the updated list and type of the newly added element.
"""

sample_list = [10,10.5,"Hello",False,[]]
for element in sample_list:
    print(f"Type of {element}",type(element))

dictionary = {
    "name" : "Ashim",
    "age" : 19,
    "is_student" :True,
    "languages" :["Java","Python","Django"]
}

sample_list.append(dictionary)
print("========================================")
print(sample_list)

print(len(sample_list))
print(type(sample_list[len(sample_list)-1]))