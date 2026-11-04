Task6
Railway Passenger Fare Calculation and Concession System
1. Problem Statement
To develop a Python program that calculates railway ticket fares based on passenger age, travel distance, and travel class. The program applies fare rates according to distance slabs, provides concessions for senior citizens and children, adds reservation fees, and calculates the final ticket amount.
2. Objectives
1.	To accept passenger details and travel information.
2.	To calculate fares using distance-based rates.
3.	To apply additional charges based on travel class.
4.	To provide concessions for senior citizens and children.
5.	To add reservation fees.
6.	To calculate the final payable amount.
7.	To identify invalid passenger details.
3. Assumptions
1.	Number of passengers must be a positive integer.
2.	Passenger age and travel distance must be greater than zero.
3.	First 100 km costs ₹1 per km.
4.	Next 400 km costs ₹1.50 per km.
5.	Above 500 km costs ₹2 per km.
6.	Sleeper class has an additional charge of ₹100.
7.	AC class has an additional charge of ₹300.
8.	Senior citizens (60 years and above) receive a 40% concession.
9.	Children below 12 years receive a 50% concession.
10.	Reservation fee is ₹50 per passenger.
4. Algorithm
1.	Start the program.
2.	Enter the number of passengers.
3.	Accept passenger name, age, distance, and travel class.
4.	Validate passenger details.
5.	Calculate fare using distance-based slabs.
6.	Add charges according to travel class.
7.	Apply age-based concessions.
8.	Add reservation fee.
9.	Calculate the final payable amount.
10.	Repeat for all passengers.
11.	Stop the program.
Test case
Test Case 1: Passenger Booking
Input:
Passengers: 3
Passenger 1: jessy, Age: 18, Distance: 18, Class: sleeper
Passenger 2: habiba, Age: 20, Distance: 10, Class: sleeper
Passenger 3: mintu, Age: 18, Distance: 18, Class: ac

Expected output:
Invalid travel class
Invalid travel class
Invalid travel class

5. Flowchart

   <img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/4a4871e5-597c-484a-9cbf-4dd692dcdad0" />

 
7. Pseudocode
START

INPUT number_of_passengers

FOR each passenger:

    INPUT name, age, distance, travel_class

    IF age <= 0 OR distance <= 0:
        DISPLAY "Invalid passenger details"
        CONTINUE

    IF distance <= 100:
        fare = distance * 1

    ELSE IF distance <= 500:
        fare = 100 + (distance - 100) * 1.5

    ELSE:
        fare = 100 + 600 + (distance - 500) * 2

    IF travel_class == "Sleeper":
        fare = fare + 100

    ELSE IF travel_class == "AC":
        fare = fare + 300

    ELSE:
        DISPLAY "Invalid travel class"
        CONTINUE

    IF age >= 60:
        concession = fare * 0.40

    ELSE IF age < 12:
        concession = fare * 0.50

    ELSE:
        concession = 0

    reservation_fee = 50

    total = fare - concession + reservation_fee

    DISPLAY total

END FOR

STOP
7. Conclusion
The Railway Passenger Fare Calculation System calculates ticket fares based on travel distance and class. It applies concessions for children and senior citizens and adds reservation fees. The program demonstrates Python conditional statements, loops, and arithmetic operations.
Note: Your original code calculates the final fare but does not display it. Add print("Total Fare:", round(total, 2)) after the total calculation to display the result.

<img width="940" height="484" alt="image" src="https://github.com/user-attachments/assets/610f124d-911d-451e-94a6-d3dd0a3a041f" />
 
