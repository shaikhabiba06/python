n = int(input("Enter number of mobile plans: "))

budget = float(input("Enter your budget: "))
usage = float(input("Enter monthly data usage in GB: "))
validity = int(input("Enter required validity in days: "))

plans = []

for i in range(n):
    print("\nPlan", i + 1)

    name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data = float(input("Enter data limit in GB: "))
    days = int(input("Enter plan validity in days: "))
    extra_charge = float(input("Enter extra charge per GB: "))

    if price < 0 or data < 0 or days <= 0 or extra_charge < 0:
        print("Invalid plan details")
    else:
        if usage > data:
            excess = usage - data
            total = price + excess * extra_charge
        else:
            excess = 0
            total = price

        if days >= validity and total <= budget:
            plans.append([name, total, excess])
            print("Eligible Plan")
        else:
            print("Not Eligible")

print("\nMobile Plan Comparison")

if len(plans) > 0:
    plans.sort(key=lambda x: x[1])

    for i in range(len(plans)):
        print("\nPlan:", plans[i][0])
        print("Total Cost:", round(plans[i][1], 2))
        print("Excess Data:", round(plans[i][2], 2), "GB")

    print("\nMost Economical Plan:", plans[0][0])
    print("Minimum Cost:", round(plans[0][1], 2))
else:
    print("No eligible mobile plans available")