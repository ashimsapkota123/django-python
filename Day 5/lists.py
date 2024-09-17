fruits = ["apple","banana","orange"]

fruits = fruits[:2]
print(fruits)


my_portfolio = [{"name":"Ashim Sapkota","age": 19},"Python","Description"]
if "Python" in my_portfolio:
    print("Python")
else:
    print("Not.")


my_portfolio[1:3] = ["Java","Nepal"]
print(my_portfolio)

my_portfolio.insert(1,"JS")
print(my_portfolio)

my_portfolio.append("React")
print(my_portfolio)

my_portfolio.extend(fruits)
print(my_portfolio)

my_portfolio.remove("Pokhara")
print(my_portfolio)

my_portfolio.pop(0)
print(my_portfolio)

my_portfolio.pop()
print(my_portfolio)

del my_portfolio[1]
print(my_portfolio)

a = my_portfolio.pop(0)
print(a)
print(my_portfolio)

my_portfolio.clear()
print(my_portfolio)

