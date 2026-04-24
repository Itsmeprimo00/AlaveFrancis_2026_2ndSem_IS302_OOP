product_FGA = input("Enter product name: ")
price_FGA = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_FGA + "," + price_FGA + "\n")

print("Product saved successfully")

