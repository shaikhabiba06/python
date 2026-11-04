Task5
Mobile Plan Comparison and Selection System
1. Problem Statement
To develop a Python program that compares different mobile plans based on budget, monthly data usage, and required validity. The program calculates extra data charges, identifies eligible plans, compares their total costs, and selects the most economical plan.
2. Objectives
1.	To accept user budget, data usage, and required validity.
2.	To collect details of different mobile plans.
3.	To calculate additional data charges.
4.	To check plan eligibility based on budget and validity.
5.	To compare the costs of eligible plans.
6.	To sort plans based on total cost.
7.	To identify the most economical mobile plan.
3. Assumptions
1.	Number of mobile plans must be a positive integer.
2.	Plan price and extra charges must be non-negative.
3.	Data limit must be non-negative.
4.	Plan validity must be greater than zero.
5.	Monthly data usage is entered in GB.
6.	Plans must satisfy the required validity.
7.	Total plan cost must not exceed the user's budget.
8.	The plan with the lowest total cost is considered the most economical.
4. Algorithm
1.	Start the program.
2.	Enter the number of mobile plans.
3.	Accept budget, monthly data usage, and required validity.
4.	Enter details of each mobile plan.
5.	Validate the plan details.
6.	Calculate excess data usage and additional charges.
7.	Calculate the total plan cost.
8.	Check whether the plan satisfies budget and validity conditions.
9.	Store eligible plans.
10.	Sort eligible plans based on total cost.
11.	Display eligible plans and their costs.
12.	Identify the most economical plan.
13.	If no plans are eligible, display a suitable message.
14.	Stop the program.
Test case
Test Case 1: Mobile Plan Comparison
Input:
Budget: 50000
Monthly data usage: 8 GB
Required validity: 40 days

Plan 1: 20days plan
Price: 20000
Data: 5 GB
Validity: 40 days
Extra charge: 300

Plan 2: 30days plan
Price: 3000
Data: 3 GB
Validity: 20 days
Extra charge: 200

Expected output:
Plan 1: Eligible
Plan 2: Not Eligible
Minimum Cost: 20900.0

6.	Flowchart

   <img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/375c136a-844b-47b6-a9ad-448c37deae3b" />

8.	 
6. Pseudocode
START

INPUT number_of_plans
INPUT budget
INPUT usage
INPUT required_validity

CREATE empty list plans

FOR each plan:

    INPUT name, price, data, days, extra_charge

    IF price < 0 OR data < 0 OR days <= 0
       OR extra_charge < 0:

        DISPLAY "Invalid plan details"

    ELSE:

        IF usage > data:
            excess = usage - data
            total = price + excess * extra_charge
        ELSE:
            excess = 0
            total = price

        IF days >= validity AND total <= budget:
            ADD plan to eligible plans
        ELSE:
            DISPLAY "Not Eligible"

END FOR

IF eligible plans exist:

    SORT plans by total cost

    DISPLAY eligible plans
    DISPLAY most economical plan

ELSE:
    DISPLAY "No eligible mobile plans"

STOP
7. Conclusion
The Mobile Plan Comparison System compares mobile plans based on budget, data usage, and validity. It calculates additional charges, identifies eligible plans, and selects the most economical option using Python conditional statements, loops, lists, and sorting.

<img width="940" height="495" alt="image" src="https://github.com/user-attachments/assets/d2c0b04f-73a9-40a9-85aa-dbdc38cd8158" />
