Task2
Electricity Bill Calculation and Monthly Comparison System
1. Problem Statement
To develop a Python program that calculates electricity bills based on monthly unit consumption using different tariff rates. The program includes fixed charges, surcharges, and rebates. It also compares monthly bills and identifies unusual increases in electricity charges.
2. Objectives
1.	To accept the number of months and electricity units consumed.
2.	To calculate electricity charges using slab rates.
3.	To add fixed charges and surcharges.
4.	To provide rebates for consumption below 100 units.
5.	To calculate and display monthly electricity bills.
6.	To compare consecutive monthly bills.
7.	To detect unusual increases in electricity bills.
3. Assumptions
1.	Number of months must be a positive integer.
2.	Electricity units are entered as numerical values.
3.	First 100 units cost ₹2 per unit.
4.	Next 100 units cost ₹3 per unit.
5.	Next 100 units cost ₹5 per unit.
6.	Above 300 units cost ₹7 per unit.
7.	Fixed charge is ₹50.
8.	Surcharge is 5% of the bill.
9.	Consumption below 100 units receives a 5% rebate.
10.	An increase above 25% compared to the previous month is considered unusual.
4. Algorithm
1.	Start the program.
2.	Accept the number of months.
3.	Create an empty list to store monthly bills.
4.	Enter electricity units for each month.
5.	Calculate the bill using slab rates.
6.	Add fixed charges and a 5% surcharge.
7.	Apply a 5% rebate if consumption is below 100 units.
8.	Store and display the monthly bill.
9.	Compare consecutive monthly bills.
10.	Detect unusual increases or decreases.
11.	Stop the program.
Test case
Test Case 1: Electricity Bill Comparison
Input:
Month 1 units: 10
Month 2 units: 10
Month 3 units: 10

Expected output:
Month 1 Bill: 67.45
Month 2 Bill: 67.45
Bill Decreased or Remained Same
Month 3 Bill: 67.45
Bill Decreased or Remained Same


Flow chart

<img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/df9d4576-eb71-42cd-a718-4996f182eda7" />


 
          6. Pseudocode
START

INPUT number_of_months

CREATE empty list bills

FOR each month:

    INPUT electricity_units

    IF units <= 100:
        bill = units * 2

    ELSE IF units <= 200:
        bill = 100*2 + (units-100)*3

    ELSE IF units <= 300:
        bill = 100*2 + 100*3 + (units-200)*5

    ELSE:
        bill = 100*2 + 100*3 + 100*5
               + (units-300)*7

    fixed_charge = 50
    surcharge = bill * 0.05

    total = bill + fixed_charge + surcharge

    IF units < 100:
        rebate = total * 0.05
        total = total - rebate

    ADD total TO bills

    DISPLAY total

END FOR

FOR each month:

    DISPLAY monthly bill

    IF month > 1:

        increase = current_bill - previous_bill

        IF increase > previous_bill * 0.25:
            DISPLAY "Unusual Increase Detected"

        ELSE IF increase > 0:
            DISPLAY "Bill Increased"

        ELSE:
            DISPLAY "Bill Decreased or Remained Same"

STOP
7. Conclusion
The Electricity Bill Calculation and Monthly Comparison System calculates electricity charges using slab rates, fixed charges, surcharges, and rebates. It compares monthly bills and detects unusual increases using Python conditional statements, loops, and lists.

<img width="940" height="261" alt="image" src="https://github.com/user-attachments/assets/f4011d57-a7e5-48f6-ae03-baa7dad2a99c" />

