# assignment
"""
In 2017, Martha had two credit cards: one that she used during the whole year,
 and another that she only used for the first six months. Below you have the monthly 
 spending values from both cards. Your task is to create a new list containing total 
 monthly spending for the entirety of 2017. Round the sums to integers and print the list.
spending_card1 = [3231.22, 3039.49, 2813.55, 2271.80, 1922.53, 2335.07]
spending_card2 = [3883.04, 3073.93, 3727.18, 2340.49, 1651.91, 1585.41, 2025.84, 3367.66, 2442.75, 2395.70, 3328.55, 3453.42]
"""

spending_card1 = [3231.22, 3039.49, 2813.55, 2271.80, 1922.53, 2335.07]
spending_card2 = [3883.04, 3073.93, 3727.18, 2340.49, 1651.91, 1585.41, 2025.84, 3367.66, 2442.75, 2395.70, 3328.55, 3453.42]

total_monthly_spend = []

for i in range(len(spending_card1)):
    total_monthly_spend.append(round(spending_card1[i]+spending_card2[i]))

for j in range(len(spending_card2)-len(spending_card1)):
    total_monthly_spend.append(round(spending_card2[i+(j+1)]))


print("\n",total_monthly_spend)
print("\nTotal Spend: ",("$"),sum(total_monthly_spend))

month = ["January", "February", "March", "April","May", "June", "July", "August", "September", "October", "November","December"]

dict = {}
for i in range(len(month)):
    dict[month[i]] = total_monthly_spend[i]

print("\n All details:\n")
print(dict,"\n")


