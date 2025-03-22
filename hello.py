menu = {
    "popcorn": 6,
    "pizza": 5,
    "momos": 10,
    "chocolate": 14
}

cart = []
total = 0

print("-----------------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")  # 2f means it will display up to 2 decimal places, and 10 means spaces
print("-------------------------------")

while True:
    food = input("Enter the food (or 'q' to quit): ").lower()
    if food == "q":
        break
    elif food in menu:  # Directly checking if food is in menu keys
        cart.append(food)
    else:
        print("Item not available in the menu.")

# Display cart items
print("\nItems in cart:")
for food in cart:
    print(food)
    total += menu[food]  # Correctly adding price of each item to total

# Display total price
print(f"\nTotal Price: ${total:.2f}")  # Display the total properly
