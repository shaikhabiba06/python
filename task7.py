n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (Food/Clothing/Electronics): ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid product details")
        continue

    amount = price * quantity

    if category == "Food":
        tax = amount * 0.05
    elif category == "Clothing":
        tax = amount * 0.10
    elif category == "Electronics":
        tax = amount * 0.18
    else:
        print("Invalid category")
        continue

    total = total + amount + tax

    print("Product:", name)
    print("Quantity:", quantity)
    print("Amount:", amount)
    print("Tax:", round(tax, 2))

if total >= 5000:
    discount = total * 0.20
elif total >= 3000:
    discount = total * 0.15
elif total >= 1000:
    discount = total * 0.10
else:
    discount = 0

if discount > 1000:
    discount = 1000

final_amount = total - discount

print("\n------ RETAIL INVOICE ------")
print("Total Amount:", round(total, 2))
print("Discount:", round(discount, 2))
print("Maximum Discount Limit: 1000")
print("Final Amount:", round(final_amount, 2))
print("----------------------------")