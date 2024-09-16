#dictionaries

# Properties of dictionaries

# representation = {}
# accessed using = Key
# nature : mutable
# ordering : unordered
# duplicate value: no
# interogenous : yes
# faster

# my_dict={
#     "name" : "Ashim",
#     "age" : 19,
#     "city" : "Syangja",
#     "country" : "Nepal"

# }
# print(my_dict)

# #accessing value using key

# print(my_dict["city"])

my_dict={
    "name" : "Ashim",
    "age" : 19,
    "city" : "Syangja",
    "country" : "Nepal",
    "languages" : ["English","Hindi","Nepali"]
}

# print(my_dict.keys())
# print(my_dict.values())

# my_dict["address"] = "Syangja"
# print(my_dict)

# my_dict.update({"education":"Bachelor"})
# print(my_dict)

# my_dict.pop("languages")

# my_dict.popitem()
# print(my_dict)

# my_dict.clear()

# print("______________________________")
# print(my_dict)

# for i in my_dict:
#     print(i)

# for x in my_dict:
#     print(my_dict[x])

# for value in my_dict.values():
#     print(value)

# for key in my_dict.keys():
#     print(key)

# for key,value in my_dict.items():
#     print(key,value)

# for x in my_dict.items():
#     print(x)

another_dict = my_dict.copy()
print(another_dict)

family = {
    "my_dad" : {
        "name": "Dad",
        "age" : 44
    },
    "mom" : {
        "name" :"Jyoti",
        "age" : 36
    },
    "me": {
        "name" : "Ashim",
        "age" : 19
    }
}

for key in family.keys():
    print(key)

print(family.keys())

for value in family.values():
    print(value)

print(family.values())

print(family["me"])

print(family["me"]["name"])

for key,value in family.items():
    for inside_key,inside_value in value.items():
        print([inside_key,inside_value])
