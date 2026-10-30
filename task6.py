n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter travel distance in km: "))
    travel_class = input("Enter class (Sleeper/AC): ")

    if age <= 0 or distance <= 0:
        print("Invalid passenger details")
        continue

    if distance <= 100:
        fare = distance * 1
    elif distance <= 500:
        fare = 100 * 1 + (distance - 100) * 1.5
    else:
        fare = 100 * 1 + 400 * 1.5 + (distance - 500) * 2

    if travel_class == "Sleeper":
        fare = fare + 100
    elif travel_class == "AC":
        fare = fare + 300
    else:
        print("Invalid travel class")
        continue

    concession = 0

    if age >= 60:
        concession = fare * 0.40
    elif age < 12:
        concession = fare * 0.50

    reservation_fee = 50

    total = fare - concession + reservation_fee

    print("\n------ Railway Ticket ------")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Distance:", distance, "km")
    print("Travel Class:", travel_class)
    print("Base Fare:", round(fare, 2))
    print("Age Concession:", round(concession, 2))
    print("Reservation Fee:", reservation_fee)
    print("Total Fare:", round(total, 2))

    cancel = input("Do you want to cancel the ticket? (yes/no): ")

    if cancel == "yes":
        penalty = total * 0.25
        refund = total - penalty

        print("Cancellation Penalty:", round(penalty, 2))
        print("Refund Amount:", round(refund, 2))
    else:
        print("Ticket Confirmed")