"""
Properties of tuples

representation : ()
type : tuple
indexing : yes
nature : immutable
ordering : no
duplicate values: yes
slicing : yes
methods : join, concatenate
heterogenous : yes
faster than list
"""

diff_value = ("ashim",19,False,[],{"address" : "Syangja"})

province = (
    "Koshi",
    "Gandaki",
    "Bagmati",
    "Madhesh",
    "Lumbini",
    "Karnali",
    "Far-west",
)

print(type(province))
print(len(province))

print(province[0])

print(province[-1])

print(province[2:5])

print(province[:3])

print(province[-2:])

if "Province 5" in province:
    print("Province 5 is in the list")
else:
    print("Province 5 is not in the list")

a = sorted(province)
print(a)

provinces = list(province)
provinces[1] = "Pokhara"
province = tuple(provinces)
print(province)

if "Pokhara" in province:
    index = provinces.index("Pokhara")
    provinces[index] = "Gandaki"
print(provinces)

for i in range(len(provinces)):
    if provinces[i] == "Gandaki":
        provinces[i] = "Pokhara"
print(provinces)

