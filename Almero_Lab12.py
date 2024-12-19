# Menu with food items and prices
menu = {
    "Salad": 160.00,
    "Cheeseburger": 100.00,
    "Whattabox": 275.00,
    "Iced Tea": 140.00,
    "Spaghetti": 75.00,
    "Fries": 150.00,
}

def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ₱{price:.2f}")

def calculate_change(total, cash_rendered):
    return cash_rendered - total

def take_order():
    # Asking user for dining option
    while True:
        dining_option = input("Would you like to Dine-In or Takeout? (Enter 'D' for Dine-In or 'T' for Takeout): ").strip().upper()
        if dining_option in ['D', 'T']:
            dining_option = "Dine-In" if dining_option == 'D' else "Takeout"
            break
        else:
            print("Invalid choice. Please enter 'D' or 'T'.")

    total_price = 0
    while True:
        display_menu()
        # Asking user to select a food item
        item = input("Please select an item from the menu (or type 'done' to finish): ").capitalize()

        if item.lower() == 'done':
            break

        if item in menu:
            price = menu[item]
            total_price += price
            print(f"You have added {item} for ₱{price:.2f} to your order. Current total: ₱{total_price:.2f}. ({dining_option})")
        else:
            print("Invalid item. Please choose from our menu again.")

    return total_price

def process_payment(total):
    while True:
        # Ask the user to input the cash rendered
        cash_rendered = float(input(f"Your total is ₱{total:.2f}. Please enter enough cash you are paying with: ₱"))

        if cash_rendered >= total:
            change = calculate_change(total, cash_rendered)
            print(f"Payment accepted. Your change is ₱{change:.2f}.")
            break
        else:
            print("Insufficient funds. Please input enough cash.")

def main():
    total_cost = take_order()
    process_payment(total_cost)

if __name__ == "__main__":
    main()
