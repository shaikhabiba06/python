Task9
Multi-Currency Travel Budget Analysis System
1. Problem Statement
To develop a Python program that calculates travel expenses in Indian Rupees using exchange rates and conversion fees. The program compares total expenses with the travel budget, identifies the largest expense category, and determines whether the budget is exceeded or remaining.
2. Objectives
1.	To accept travel budget and exchange rates.
2.	To collect expenses from different categories.
3.	To convert foreign currency into INR.
4.	To calculate currency conversion fees.
5.	To calculate total travel expenses.
6.	To identify the largest expense category.
7.	To compare expenses with the available budget.
3. Assumptions
1.	Number of expense categories must be a positive integer.
2.	Travel budget must be entered in INR.
3.	Exchange rate must be entered in INR per foreign currency unit.
4.	Expense amounts must be non-negative.
5.	Conversion fee is calculated as a percentage.
6.	Total expenses include conversion fees.
7.	The largest expense is identified using the final converted amount.
8.	Budget status depends on total expenses.
4. Algorithm
1.	Start the program.
2.	Enter the number of expense categories.
3.	Accept budget, exchange rate, and conversion fee.
4.	Initialize total expenses and largest expense.
5.	Enter expense category and foreign currency amount.
6.	Validate the expense amount.
7.	Convert the expense into INR.
8.	Calculate the conversion fee.
9.	Calculate the final expense amount.
10.	Update total expenses and largest expense.
11.	Repeat for all categories.
12.	Compare total expenses with the budget.
13.	Display budget status and largest expense category.
14.	Stop the program.
Test case
Test Case 1: Travel Budget Report
Input:
Categories: 2
Budget: 20000
Exchange rate: 700
Conversion fee: 20%

Expense 1: 2000, Amount: 700
Expense 2: 3000, Amount: 800

Expected output:
Total Expenses: 3150000.0
Budget Status: Budget Exceeded
Extra Spending: 3130000.0

5. Flowchart

   <img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/88898cf4-712d-4846-990b-4a7b1b8f3526" />

              
7. Pseudocode
START

INPUT number_of_categories
INPUT budget
INPUT exchange_rate
INPUT conversion_fee

total = 0
largest = 0
largest_category = ""

FOR each expense:

    INPUT category
    INPUT amount

    IF amount < 0:
        DISPLAY "Invalid expense amount"
        CONTINUE

    converted = amount * exchange_rate

    fee = converted * conversion_fee / 100

    final_amount = converted + fee

    total = total + final_amount

    IF final_amount > largest:
        largest = final_amount
        largest_category = category

END FOR

IF total > budget:
    DISPLAY "Budget Exceeded"

ELSE IF total == budget:
    DISPLAY "Budget Fully Used"

ELSE:
    DISPLAY "Within Budget"

DISPLAY total
DISPLAY largest_category

STOP
7. Conclusion
The Multi-Currency Travel Budget Analysis System converts foreign expenses into INR, calculates conversion fees, and compares total spending with the available budget. It also identifies the largest expense category using Python loops, conditional statements, and arithmetic operations.

<img width="940" height="424" alt="image" src="https://github.com/user-attachments/assets/75cae9ab-3e3f-422f-a04c-b1b673f9f684" />
