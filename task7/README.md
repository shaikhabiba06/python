Task7
Retail Billing and Discount Calculation System
1. Problem Statement
To develop a Python program that calculates product prices, quantities, and category-based taxes. The program calculates the total purchase amount, applies discounts based on the total bill, and generates the final payable amount with a maximum discount limit of ₹1,000.
2. Objectives
1.	To accept product details and quantities.
2.	To calculate the total price of products.
3.	To apply taxes based on product categories.
4.	To calculate discounts based on the total purchase amount.
5.	To limit the maximum discount to ₹1,000.
6.	To calculate the final payable amount.
7.	To generate a retail invoice.
3. Assumptions
1.	Number of products must be a positive integer.
2.	Product price must be non-negative.
3.	Quantity must be greater than zero.
4.	Food products have 5% tax.
5.	Clothing products have 10% tax.
6.	Electronics products have 18% tax.
7.	Purchases of ₹5,000 or more receive a 20% discount.
8.	Purchases of ₹3,000 or more receive a 15% discount.
9.	Purchases of ₹1,000 or more receive a 10% discount.
10.	Maximum discount is limited to ₹1,000.
4. Algorithm
1.	Start the program.
2.	Enter the number of products.
3.	Accept product name, category, price, and quantity.
4.	Validate product details.
5.	Calculate the product amount.
6.	Apply tax according to the product category.
7.	Add the amount and tax to the total bill.
8.	Repeat for all products.
9.	Calculate the discount based on the total amount.
10.	Apply the maximum discount limit of ₹1,000.
11.	Calculate the final payable amount.
12.	Display the retail invoice.
13.	Stop the program.
Test case
Test Case 1: Retail Invoice
Input:
Products: 2
Product 1: soap, electronics, 1000, Qty: 200
Product 2: cake, food, 100, Qty: 2

Expected output:
Invalid category
Invalid category
Total Amount: 0
Final Amount: 0

5. Flowchart

   <img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/b6348136-7e86-4c60-9ce7-0f94905fc209" />

 
7. Pseudocode
START

INPUT number_of_products
total = 0

FOR each product:

    INPUT name, category, price, quantity

    IF price < 0 OR quantity <= 0:
        DISPLAY "Invalid product details"

    ELSE:

        amount = price * quantity

        IF category == "Food":
            tax = amount * 0.05

        ELSE IF category == "Clothing":
            tax = amount * 0.10

        ELSE IF category == "Electronics":
            tax = amount * 0.18

        ELSE:
            DISPLAY "Invalid category"
            CONTINUE

        total = total + amount + tax

END FOR

IF total >= 5000:
    discount = total * 0.20

ELSE IF total >= 3000:
    discount = total * 0.15

ELSE IF total >= 1000:
    discount = total * 0.10

ELSE:
    discount = 0

IF discount > 1000:
    discount = 1000

final_amount = total - discount

DISPLAY total
DISPLAY discount
DISPLAY final_amount

STOP
7. Conclusion
The Retail Billing System calculates product costs, applies category-based taxes, and provides discounts according to the total purchase amount. It limits the maximum discount to ₹1,000 and generates the final invoice using Python conditional statements, loops, and arithmetic operations.

 <img width="940" height="402" alt="image" src="https://github.com/user-attachments/assets/a3ffc388-570b-454d-ab38-4dec75140709" />

