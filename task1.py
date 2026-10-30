name = input("Enter student name: ")
aggregate = float(input("Enter aggregate marks (%): "))
maths = float(input("Enter Mathematics marks (%): "))
physics = float(input("Enter Physics marks (%): "))
attendance = float(input("Enter attendance (%): "))
income = float(input("Enter annual family income (Rs.): "))

if (aggregate >= 75 and maths >= 60 and physics >= 60
        and attendance >= 75 and income <= 250000):

    print("\nCongratulations! You are eligible for the scholarship.")

    score = aggregate + attendance

    print("Student Name:", name)
    print("Ranking Score:", score)

    if aggregate >= 90:
        print("Scholarship Category: Excellent")
    elif aggregate >= 80:
        print("Scholarship Category: Merit")
    else:
        print("Scholarship Category: General")

else:
    print("\nSorry! You are not eligible for the scholarship.")

    if aggregate < 75:
        print("- Aggregate marks must be at least 75%.")
    if maths < 60:
        print("- Mathematics marks must be at least 60%.")
    if physics < 60:
        print("- Physics marks must be at least 60%.")
    if attendance < 75:
        print("- Attendance must be at least 75%.")
    if income > 250000:
        print("- Annual family income must not exceed Rs. 2,50,000.")