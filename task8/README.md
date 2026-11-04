Task8
Manufacturing Cost and Profitability Analysis System
1. Problem Statement
To develop a Python program that calculates manufacturing costs, total sales, and profit for different products. The program considers material costs, labour charges, wastage, and machine costs. It calculates profit percentage and checks whether the expected profit target is achieved or the production is running at a loss.
2. Objectives
1.	To accept product and production details.
2.	To calculate total production cost.
3.	To calculate total sales.
4.	To determine total profit or loss.
5.	To calculate profit percentage.
6.	To compare actual profit with the expected profit target.
7.	To identify whether the production is profitable.
3. Assumptions
1.	Number of products must be a positive integer.
2.	All costs and selling prices must be non-negative.
3.	Quantity produced must be greater than zero.
4.	Material, labour, wastage, and machine costs are considered per unit.
5.	Total production cost is calculated by multiplying unit cost by quantity.
6.	Total sales are calculated using selling price multiplied by quantity.
7.	Profit is calculated by subtracting total cost from total sales.
8.	Expected profit percentage must be non-negative.
4. Algorithm
1.	Start the program.
2.	Enter the number of products.
3.	Accept product name and production details.
4.	Validate all input values.
5.	Calculate total production cost.
6.	Calculate total sales.
7.	Calculate profit or loss.
8.	Calculate profit percentage.
9.	Compare profit percentage with the expected target.
10.	Display whether the production is at a loss, target achieved, or target not achieved.
11.	Repeat for all products.
12.	Stop the program.
Test case
Input:
Products: 2
Product 1: milk, Costs: 1000, 500, 100, 100
Selling price: 1500, Quantity: 200
Expected profit: 90%

Product 2: chocolate, Costs: 2000, 1, 100, 500
Selling price: 3000, Quantity: 90
Expected profit: 90%

Expected output:
Product 1: Production running at a loss
Product 2: Profit target not achieved
5. Flowchart

<img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/130ccfb9-ab68-4a5d-a549-e395ff592355" />

 
6. Pseudocode
START

INPUT number_of_products

FOR each product:

    INPUT name
    INPUT material, labour, wastage
    INPUT machine, selling, quantity, target

    IF any cost < 0 OR quantity <= 0 OR target < 0:

        DISPLAY "Invalid production details"

    ELSE:

        total_cost = (material + labour + wastage + machine) * quantity

        total_sales = selling * quantity

        profit = total_sales - total_cost

        IF total_cost > 0:
            profit_percentage = (profit / total_cost) * 100
        ELSE:
            profit_percentage = 0

        IF profit < 0:
            DISPLAY "Production is running at a loss"

        ELSE IF profit_percentage >= target:
            DISPLAY "Profit Target Achieved"

        ELSE:
            DISPLAY "Profit Target Not Achieved"

        DISPLAY manufacturing report

END FOR

STOP
7. Conclusion
The Manufacturing Cost and Profitability Analysis System calculates production costs, sales, and profit. It identifies losses and checks whether the expected profit target is achieved using Python conditional statements, loops, and arithmetic operations.

<img width="940" height="431" alt="image" src="https://github.com/user-attachments/assets/6ffbae47-63ce-4b2c-8ed1-23fa6650dff2" />
