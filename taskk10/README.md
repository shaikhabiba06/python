Task10
Campus Event Financial Planning System
1. Problem Statement
To develop a Python program that calculates campus event expenses, including venue, equipment, catering, transport, and certificate costs. The program calculates participant contributions, sponsorship amounts, financial shortfalls, and the minimum number of participants required to break even.
2. Objectives
1.	To accept event expenses and participant details.
2.	To calculate fixed and variable costs.
3.	To calculate total event expenses.
4.	To calculate participant contributions and sponsorship funds.
5.	To identify financial shortfalls.
6.	To calculate the minimum participants needed to break even.
7.	To determine the financial success of the event.
3. Assumptions
1.	All costs and contributions must be non-negative.
2.	Number of participants must be greater than zero.
3.	Venue, equipment, and transport costs are fixed costs.
4.	Catering and certificate costs depend on participants.
5.	Total funds include participant contributions and sponsorship.
6.	Break-even is possible only when participant contribution exceeds per-person variable cost.
7.	Minimum participants are calculated using the break-even formula.
4. Algorithm
1.	Start the program.
2.	Enter venue, equipment, catering, transport, and certificate costs.
3.	Enter the expected number of participants.
4.	Enter sponsorship and participant contribution.
5.	Validate all input values.
6.	Calculate fixed and variable costs.
7.	Calculate total event cost.
8.	Calculate total participant contributions and available funds.
9.	Calculate financial shortfall.
10.	Calculate minimum participants required to break even.
11.	Display financial status and event report.
12.	Stop the program.
Test case
Test Case 1: Campus Event Report
Input:
Venue: 10000
Equipment: 5000
Catering: 3000
Transport: 2000
Certificate: 1000
Participants: 5
Sponsorship: 15000
Contribution: 3000

Expected output:
Total Event Cost: 37000.0
Total Available Funds: 30000.0
Event Status: Additional Funds Required

5. Flowchart

   <img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/86ed3d61-ac94-4807-8af5-dd8d51e838d4" />

 
6. Pseudocode
START

INPUT venue, equipment, catering
INPUT transport, certificate
INPUT participants
INPUT sponsorship, contribution

IF any cost or contribution < 0
   OR participants <= 0:

    DISPLAY "Invalid event details"

ELSE:

    fixed_cost = venue + equipment + transport

    variable_cost = (catering + certificate) * participants

    total_cost = fixed_cost + variable_cost

    total_contribution = participants * contribution

    total_funds = total_contribution + sponsorship

    shortfall = total_cost - total_funds

    IF contribution > catering + certificate:

        break_even = CEILING(
            fixed_cost / (contribution - catering - certificate)
        )

    ELSE:
        break_even = -1

    IF shortfall > 0:
        DISPLAY "Financial Shortfall"

    ELSE:
        DISPLAY "Sufficient Funds"

    IF break_even == -1:
        DISPLAY "Break-even Cannot Be Achieved"

    ELSE:
        DISPLAY break_even

    IF total_funds >= total_cost:
        DISPLAY "Financially Successful"

    ELSE:
        DISPLAY "Additional Funds Required"

    DISPLAY Event Report

STOP
7. Conclusion
The Campus Event Financial Planning System calculates event expenses, participant contributions, and sponsorship funds. It identifies financial shortfalls and determines the minimum participants required to break even using Python conditional statements, arithmetic operations, and type conversions.

<img width="940" height="468" alt="image" src="https://github.com/user-attachments/assets/4d6a32ba-fdf2-40c9-9312-73f62db5f6d9" />
 



