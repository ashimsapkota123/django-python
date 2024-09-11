"""
Properties of set

representation : {}
type : set
indexing : no
nature : mutable
ordering : no
duplicate values: no
slicing : no
methods : union, intersection,asymetric difference
heterogenous : yes
"""

#define a set of vehicles

vehicles = {"car","bus"}
print(vehicles)

# 0 is false and 1 is true 

test = {False,0,1,True}
print(test)

# print the length
print(len(test))

#print vehicles using for loop
for vehicle in vehicles:
    print(vehicle)

# check if aeroplane is in the vehicles or not
if "aeroplane" in vehicles:
    print("aeroplane is in the vehicles")
else:
    print("aeroplane is not in the vehicles")

#adding element to set , if helicopter is not present add
# if "helicopter" not in vehicles:
#     vehicles.add("helicopter")

if "helicopter" in vehicles:
    pass
else:
    vehicles.add("helicopter")

#update
#create another list of vehciles used in water and update to vehciles set
water_vehicals = {"Ship","Ferri","Submamrine"}
vehicles.update(water_vehicals)
print(vehicles)

#remove car from  the set 

vehicles.remove("car")

#discard can be used to find and remove and doesnot throw error if not found
vehicles.discard("car")
print(vehicles)

#set methods 
petrol_engine = {"bike","scooter","car"}
diesel_engine = {"bus","truck","car"}

union = petrol_engine.union(diesel_engine)
print(union)

print(petrol_engine|diesel_engine)

intersection = petrol_engine.intersection(diesel_engine)
print(petrol_engine & diesel_engine)
print(intersection)





