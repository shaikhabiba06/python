n = int(input("Enter number of expense categories: "))

budget = float(input("Enter total travel budget in INR: "))
rate = float(input("Enter exchange rate (1 foreign currency in INR): "))
fee = float(input("Enter conversion fee percentage: "))

total = 0
largest = 0
largest_category = ""

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount in foreign currency: "))

    if amount < 0:
        print("Invalid expense amount")
        continue

    converted = amount * rate
    conversion_fee = converted * fee / 100
    final_amount = converted + conversion_fee

    total = total + final_amount

    if final_amount > largest:
        largest = final_amount
        largest_category = category

    print("Category:", category)
    print("Converted Amount:", round(converted, 2))
    print("Conversion Fee:", round(conversion_fee, 2))
    print("Final Expense in INR:", round(final_amount, 2))

print("\n------ TRAVEL BUDGET REPORT ------")
print("Total Travel Expenses:", round(total, 2))
print("Travel Budget:", round(budget, 2))
print("Largest Expense Category:", largest_category)
print("Largest Expense:", round(largest, 2))

if total > budget:
    print("Budget Status: Budget Exceeded")
    print("Extra Spending:", round(total - budget, 2))
elif total == budget:
    print("Budget Status: Budget Fully Used")
else:
    print("Budget Status: Within Budget")
    print("Remaining Budget:", round(budget - total, 2))

print("----------------------------------")