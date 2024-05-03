def display_menu(products):
    print("\nWelcome to the Vending Machine")
    for category, items in products.items():
        print(f"{category}:\n")
        print("Code\tProduct\t\tPrice\tQuantity")
        for code, product in items.items():
            print(f"{code}\t{product['name']}\t\t${product['price']:.2f}\t{product['quantity']}")

def select_product(products, balance):
    while True:
        code = input("\nEnter the product code: ").upper()
        category, product = None, None
        for cat, items in products.items():
            if code in items:
                category = cat
                product = items[code]
                break
        if product:
            while product['quantity'] > 0 and balance < product['price']:
                print("\nInsufficient balance. Please insert more money.")
                balance = insert_money(balance)
            if product['quantity'] > 0:
                balance -= product['price']
                product['quantity'] -= 1
                print(f"\nDispensing {product['name']}...")
                print(f"Remaining Balance: ${balance:.2f}")
                print(f"Remaining {product['name']} quantity: {product['quantity']}")
                return category, code
            elif product['quantity'] == 0:
                print("\nSorry, this product is out of stock.")
            else:
                print("\nInsufficient balance. Please insert more money.")
        else:
            print("\nInvalid choice. Please enter a valid product code.")

def insert_money(balance):
    while True:
        money_input = input("\nInsert money (in dollars): ")
        if money_input.replace('.', '', 1).isdigit():
            money = float(money_input)
            if money > 0:
                balance += money
                print(f"Current Balance: ${balance:.2f}")
                break
            elif money < 0:
                print("Invalid amount. Please insert a positive amount.")
            else:
                print("Enter the currency in digit form.")
        else:
            print("Invalid input. Please enter a numeric amount.")
    return balance

def vending_machine(products):
    display_menu(products)
    balance = 0
    total_spent = 0
    while True:
        if balance <= 0:
            balance = insert_money(balance)
        selected_category, selected_code = select_product(products, balance)
        if selected_category and selected_code:
            total_spent += products[selected_category][selected_code]['price']
            balance -= products[selected_category][selected_code]['price']
            more_purchase = input("\nDo you want to make another purchase? (yes/no): ").lower()
            if more_purchase == 'no':
                change = balance if balance >= 0 else 0
                print(f"Total spent: ${total_spent:.2f}")
                print(f"Change: ${change:.2f}")
                print("Thank you for using the Vending Machine. Goodbye!")
                break

# Sample products for the vending machine
products = {
    'Snacks': {
        'A1': {'name': 'Chips', 'price': 1.50, 'quantity': 10},
        'A2': {'name': 'Candy', 'price': 1.00, 'quantity': 8},
        'A3': {'name': 'Popcorn', 'price': 2.00, 'quantity': 15},
        'A4': {'name': 'Pretzels', 'price': 1.75, 'quantity': 12},
        'A5': {'name': 'Chocolate Bar', 'price': 2.25, 'quantity': 10},
        'A6': {'name': 'Cookies', 'price': 1.80, 'quantity': 10},
        'A7': {'name': 'Trail Mix', 'price': 2.50, 'quantity': 8},
        'A8': {'name': 'Granola Bars', 'price': 1.50, 'quantity': 12},
        'A9': {'name': 'Peanuts', 'price': 1.25, 'quantity': 15},
        'A10': {'name': 'Rice Crispy Treat', 'price': 2.00, 'quantity': 10}
    },
    'Drinks': {
        'B1': {'name': 'Water', 'price': 1.00, 'quantity': 12},
        'B2': {'name': 'Soda', 'price': 1.50, 'quantity': 10},
        'B3': {'name': 'Juice', 'price': 2.00, 'quantity': 20},
        'B4': {'name': 'Iced Tea', 'price': 1.75, 'quantity': 15},
        'B5': {'name': 'Energy Drink', 'price': 2.50, 'quantity': 8},
        'B6': {'name': 'Coffee', 'price': 2.00, 'quantity': 10},
        'B7': {'name': 'Milk', 'price': 1.50, 'quantity': 12},
        'B8': {'name': 'Sports Drink', 'price': 2.25, 'quantity': 10},
        'B9': {'name': 'Lemonade', 'price': 2.00, 'quantity': 10},
        'B10': {'name': 'Fruit Smoothie', 'price': 3.00, 'quantity': 8}
    },
    'Sandwiches': {
        'C1': {'name': 'Turkey Sandwich', 'price': 4.50, 'quantity': 6},
        'C2': {'name': 'Ham and Cheese Sandwich', 'price': 4.25, 'quantity': 8},
        'C3': {'name': 'Vegetarian Sandwich', 'price': 4.00, 'quantity': 10},
        'C4': {'name': 'Chicken Caesar Wrap', 'price': 5.00, 'quantity': 6},
        'C5': {'name': 'Tuna Salad Sandwich', 'price': 4.75, 'quantity': 8},
        'C6': {'name': 'Egg Salad Sandwich', 'price': 4.25, 'quantity': 10},
        'C7': {'name': 'BLT Sandwich', 'price': 5.25, 'quantity': 6},
        'C8': {'name': 'Club Sandwich', 'price': 5.50, 'quantity': 8},
        'C9': {'name': 'Grilled Cheese Sandwich', 'price': 3.75, 'quantity': 10},
        'C10': {'name': 'Peanut Butter & Jelly Sandwich', 'price': 3.50, 'quantity': 8}
    },
    'Salads': {
        'D1': {'name': 'Caesar Salad', 'price': 5.50, 'quantity': 6},
        'D2': {'name': 'Greek Salad', 'price': 6.00, 'quantity': 8},
        'D3': {'name': 'Cobb Salad', 'price': 6.25, 'quantity': 10},
        'D4': {'name': 'Chef Salad', 'price': 6.50, 'quantity': 6},
        'D5': {'name': 'Spinach Salad', 'price': 5.75, 'quantity': 8},
        'D6': {'name': 'Nicoise Salad', 'price': 6.75, 'quantity': 10},
        'D7': {'name': 'Caprese Salad', 'price': 6.00, 'quantity': 6},
        'D8': {'name': 'Waldorf Salad', 'price': 6.25, 'quantity': 8},
        'D9': {'name': 'Fruit Salad', 'price': 4.50, 'quantity': 10},
        'D10': {'name': 'Chicken Caesar Salad', 'price': 7.00, 'quantity': 8}
    }
}

vending_machine(products)