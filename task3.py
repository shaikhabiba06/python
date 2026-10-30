n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))
    payment = input("Enter payment type (Cash/Insurance): ")

    if age <= 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid billing details")
    else:
        total = consultation + diagnostic + treatment

        if age >= 60:
            concession = total * 0.20
        elif age < 12:
            concession = total * 0.10
        else:
            concession = 0

        final_bill = total - concession

        if payment == "Insurance":
            final_bill = final_bill * 0.80
            category = "Insurance Patient"
        elif payment == "Cash":
            category = "Self-Paying Patient"
        else:
            print("Invalid payment type")
            continue

        print("\nPatient Name:", name)
        print("Total Charges:", total)
        print("Concession:", concession)
        print("Final Bill:", round(final_bill, 2))
        print("Patient Classification:", category)

        if final_bill <= 1000:
            print("Payment Category: Low")
        elif final_bill <= 5000:
            print("Payment Category: Medium")
        else:
            print("Payment Category: High")