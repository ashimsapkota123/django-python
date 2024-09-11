"""
Playing with data types
"""

"""
Create Data Structures:
Use a list to store product details. Each product is a dictionary with keys: name, category, and price.
Use a tuple to store immutable product categories (e.g., ("Electronics", "Clothing", "Food")).
Use a set to keep track of all unique prices in the inventory.
Perform Operations:
Add a Product: Write a function to add a new product to the list. The function should accept name, category, and price, then add a dictionary representing the product to the list. Update the set of prices.
Update a Product: Write a function to update the price of a product given its name. Update the set of prices accordingly.
Delete a Product: Write a function to remove a product by name. Ensure the set of prices is updated.
List Products by Category: Write a function to display all products in a given category.
Check Category Validity: When adding a product, check if the category is valid by comparing it to the categories in the tuple.
"""

store_product_details = []
product_categories = ("Electronics","Clothing","Food")
unique_prices = set()

def add_new_product(name,category,price):
    if category in product_categories:
        product = {"name":name,"category":category,"price":price}
        store_product_details.append(product)
        unique_prices.add(price)
        return print(f"Product {name} added successfully.")
    else:
        print("Invalid Category. Please enter valid category.")

def update__price_product(name,new_price):
    for product in store_product_details:
        if product["name"] == name:
            unique_prices.discard(product["price"])
            product["price"] = new_price
            unique_prices.add(new_price)
            return print(f"Product {name} price update Successfully.")
    return print("Product not found.")

def delete_product(name):
    for product in store_product_details:
        if product["name"] == name:
            unique_prices.discard(product["price"])
            store_product_details.remove(product)
            return print(f"Product {name} delete successfully.")
    return print("Product not found.")

def list_of_products_by_catogories(category):
    for product in store_product_details:
        if product["category"] == category:
            print(product["name"])

#add product by user
name = input("Enter product name: ")
category = input("Enter product category: ")
price = int(input("Enter product price: "))
add_new_product(name,category,price)

add_new_product("Charger", "Electronics", 350)
add_new_product("Socks", "Clothing",100)
add_new_product("Pants", "Clothing",3200)
add_new_product("MO:MO", "Food", 100)
add_new_product("Mango", "Food", 350)

#update product
update_name = input("Enter a product name to update it's price:")
update_price = int(input("Enter new price:"))
update__price_product(update_name,update_price)


update__price_product("Headphone", 1200)
update__price_product("MO:MO",120)

#delete product
delete_name = input("Enter a product name for delete: ")
delete_name(delete_product)
delete_product("Pants")

list_of_products_by_catogories("Electronics")

print("Unique prices:", unique_prices)


