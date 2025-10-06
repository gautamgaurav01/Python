cart = {}


def add_items():
    name = input("Enter items name: ").upper()
    price = input("Enter items price: ")
    quantity = input("Enter items quantity: ")
    cart[name] = {"item": name, "price": price, "quantity": quantity}


def remove_items():
    name = input("Enter the item name you want to remove: ").upper()
    if name in cart:
        del cart[name]
        print(f"{name} removed from cart.\n")
    else:
        print(f"{name} not found in cart.\n")


def view_cart():
    if not cart:
        print("Cart is empty.\n")
        return
    print("\nItems in your cart:")
    for name, details in cart.items():
        print(
            f"Name: {name}, Price: Rs.{details['price']}, Quantity: {details['quantity']}"
        )


while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            add_items()
        case "2":
            remove_items()
        case "3":
            view_cart()
        case "4":
            print("Exiting... Thank you for shopping!")
            break
        case _:
            print("Invalid choice. Try again.\n")
    print(cart)
