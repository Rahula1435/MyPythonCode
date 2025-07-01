quantity = int(input("Enter the quantity of items: "))

price_per_item = float(input("Enter the price of each item: "))

total_expense = quantity * price_per_item

if total_expense > 5000:
    discount = total_expense * 0.10
    total_expense -= discount
    print(f"A 10% discount of {discount} has been applied.")

print("Total expense after discount :", total_expense)
