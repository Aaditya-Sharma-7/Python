#Define the menu of restaurant

menu = {
    'Pizza':50,
    'Pasta':60,
    'Salad':40,
    'Burger':70,
    'Coffee':80,
}

#Greet
print("Welcome to PYTHON Restorant")
print("Pizza: Rs50\nPasta: Rs60\nSalad: Rs40\nBurger: Rs70\nCoffee: Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order :")
if item_1 in menu:
    order_total += menu[item_1]
    print(f'Your item{item_1} has been added to your order')

else:
    print(f'Ordered item {item_1} is not available yet!\nPlease order something else')

another_order = input("Do you want to add another item? (Yes/No) : ")

if another_order == "Yes" or "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'Item{item_2} has been added to order')
    else:
        print(f'order item {item_2} is not available')

else:
    pass

print(f'The total amount of items to pay is :- {order_total}')