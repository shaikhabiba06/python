n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    name = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowances: "))
    overtime = float(input("Enter overtime amount: "))
    incentive = float(input("Enter incentives: "))

    if basic < 0 or allowance < 0 or overtime < 0 or incentive < 0:
        print("Invalid salary details")
    else:
        gross = basic + allowance + overtime + incentive

        if gross <= 20000:
            deduction = gross * 0.05
        elif gross <= 40000:
            deduction = (20000 * 0.05) + (gross - 20000) * 0.10
        elif gross <= 60000:
            deduction = (20000 * 0.05) + (20000 * 0.10) + (gross - 40000) * 0.15
        else:
            deduction = (20000 * 0.05) + (20000 * 0.10) + (20000 * 0.15) + (gross - 60000) * 0.20

        net_salary = gross - deduction

        print("\n------ Salary Statement ------")
        print("Employee Name:", name)
        print("Basic Salary:", basic)
        print("Allowances:", allowance)
        print("Overtime:", overtime)
        print("Incentives:", incentive)
        print("Gross Salary:", round(gross, 2))
        print("Total Deduction:", round(deduction, 2))
        print("Net Salary:", round(net_salary, 2))
        print("------------------------------")