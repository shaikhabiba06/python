Task4
Employee Salary Calculation and Payroll Management System
1. Problem Statement
To develop a Python program that calculates employee salaries based on basic salary, allowances, overtime, and incentives. The program calculates gross salary, applies deductions using different salary slabs, and determines the final net salary for each employee.
2. Objectives
1.	To accept employee details and salary components.
2.	To calculate gross salary.
3.	To apply deductions based on salary slabs.
4.	To calculate total deductions.
5.	To determine the final net salary.
6.	To generate an individual salary statement.
7.	To identify invalid salary details.
3. Assumptions
1.	Number of employees must be a positive integer.
2.	Employee name is entered as a string.
3.	All salary components must be non-negative.
4.	Gross salary is calculated by adding basic salary, allowances, overtime, and incentives.
5.	Salary up to ₹20,000 has a 5% deduction.
6.	Salary from ₹20,001 to ₹40,000 has a 10% deduction on the additional amount.
7.	Salary from ₹40,001 to ₹60,000 has a 15% deduction on the additional amount.
8.	Salary above ₹60,000 has a 20% deduction on the additional amount.
4. Algorithm
1.	Start the program.
2.	Enter the number of employees.
3.	Accept employee name and salary details.
4.	Check whether all salary components are valid.
5.	Calculate gross salary.
6.	Calculate deductions using salary slabs.
7.	Calculate net salary by subtracting deductions from gross salary.
8.	Display the employee salary statement.
9.	Repeat for all employees.
10.	Stop the program.
Test case
Test Case 1: Employee Salary Calculation
Input:
Number of employees: 2

Employee 1: rishi
Basic salary: 30000
Allowances: 3000
Overtime: 5000
Incentives: 2500

Employee 2: siri
Basic salary: 30000
Allowances: 3000
Overtime: 2000
Incentives: 25000

Expected output:
Employee 1 Net Salary: 37425.0
Employee 2 Net Salary: 54000.0

5. Flowchart

6. <img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/8d131848-a532-49db-ba63-2755d7ab9fe2" />

           
7. Pseudocode
START

INPUT number_of_employees

FOR each employee:

    INPUT name
    INPUT basic_salary
    INPUT allowance
    INPUT overtime
    INPUT incentive

    IF any salary component < 0:
        DISPLAY "Invalid salary details"

    ELSE:

        gross = basic + allowance + overtime + incentive

        IF gross <= 20000:
            deduction = gross * 0.05

        ELSE IF gross <= 40000:
            deduction = 1000 + (gross - 20000) * 0.10

        ELSE IF gross <= 60000:
            deduction = 3000 + (gross - 40000) * 0.15

        ELSE:
            deduction = 6000 + (gross - 60000) * 0.20

        net_salary = gross - deduction

        DISPLAY salary statement

END FOR

STOP
7. Conclusion
The Employee Salary Calculation System calculates gross salary, applies slab-based deductions, and determines net salary. It uses Python conditional statements, loops, and arithmetic operations to generate employee salary statements accurately.

<img width="940" height="487" alt="image" src="https://github.com/user-attachments/assets/9f5f596e-2646-47d1-a4c8-2fc5f50e9b5d" />
