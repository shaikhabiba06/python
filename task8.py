n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    material = float(input("Enter material cost: "))
    labour = float(input("Enter labour charges: "))
    wastage = float(input("Enter wastage cost: "))
    machine = float(input("Enter machine cost: "))
    selling = float(input("Enter selling price: "))
    quantity = int(input("Enter quantity produced: "))
    target = float(input("Enter expected profit percentage: "))

    if material < 0 or labour < 0 or wastage < 0 or machine < 0 or selling < 0 or quantity <= 0 or target < 0:
        print("Invalid production details")
    else:
        total_cost = (material + labour + wastage + machine) * quantity
        total_sales = selling * quantity

        profit = total_sales - total_cost

        profit_percentage = (profit / total_cost) * 100 if total_cost > 0 else 0

        print("\n------ MANUFACTURING REPORT ------")
        print("Product Name:", name)
        print("Total Production Cost:", round(total_cost, 2))
        print("Total Sales:", round(total_sales, 2))
        print("Total Profit:", round(profit, 2))
        print("Profit Percentage:", round(profit_percentage, 2), "%")

        if profit < 0:
            print("Result: Production is running at a loss")
        elif profit_percentage >= target:
            print("Result: Profit Target Achieved")
        else:
            print("Result: Profit Target Not Achieved")

        print("----------------------------------")