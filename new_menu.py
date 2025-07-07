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

while True:
    choice = int(input("order for 1 or exit for 0 :- "))
    if choice == 1:
        item_1 = input("Enter the name of item you want to order :")
        if item_1 in menu:
            order_total += menu[item_1]
            print(f'Your item{item_1} has been added to your order')

        else:
            print(f'Ordered item {item_1} is not available yet!\nPlease order something else')

        print(f'The total amount of items to pay is :- {order_total}')
    
    elif choice == 0:
        print("thank you for order")
        break
    else:
        print("Invalid value")