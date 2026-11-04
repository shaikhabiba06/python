Task3
Hospital Patient Billing and Payment Classification System
1. Problem Statement
To develop a Python program that calculates hospital bills based on consultation, diagnostic, and treatment charges. The program provides concessions based on patient age, applies insurance discounts, classifies patients according to payment type, and categorizes the final bill as Low, Medium, or High.
2. Objectives
1.	To collect patient details and billing information.
2.	To calculate total hospital charges.
3.	To provide concessions for senior citizens and children.
4.	To apply discounts for insurance patients.
5.	To classify patients based on payment type.
6.	To calculate the final payable amount.
7.	To categorize payments as Low, Medium, or High.
8.	To identify invalid billing details.
3. Assumptions
1.	Number of patients must be a positive integer.
2.	Patient name is entered as a string.
3.	Patient age must be greater than zero.
4.	All hospital charges must be non-negative.
5.	Senior citizens (60 years and above) receive a 20% concession.
6.	Children below 12 years receive a 10% concession.
7.	Insurance patients receive an additional 20% discount.
8.	Payment types are Cash or Insurance.
9.	Final bills up to ₹1,000 are Low, up to ₹5,000 are Medium, and above ₹5,000 are High.
4. Algorithm
1.	Start the program.
2.	Enter the number of patients.
3.	Accept patient name, age, consultation, diagnostic, and treatment charges.
4.	Enter payment type.
5.	Check whether age and charges are valid.
6.	Calculate total hospital charges.
7.	Apply age-based concessions.
8.	Check payment type and apply insurance discount if applicable.
9.	Calculate the final bill.
10.	Classify the patient as Insurance or Self-Paying.
11.	Categorize the final payment as Low, Medium, or High.
12.	Repeat for all patients.
13.	Stop the program.
Test case
Test Case 1: Patient Billing System
Input:
Number of patients: 2

Patient 1:
Name: sirisha
Age: 30
Consultation charges: 500
Diagnostic charges: 300
Treatment charges: 400
Payment type: cash

Patient 2:
Name: rithu
Age: 20
Consultation charges: 500
Diagnostic charges: 300
Treatment charges: 300
Payment type: cash

Expected output:
Invalid payment type
Invalid payment type

5. Flowchart

6. <img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/5114bd75-e9e5-41b5-8d82-30d182250ff7" />


 
7. Pseudocode
START

INPUT number_of_patients

FOR each patient:

    INPUT name
    INPUT age
    INPUT consultation
    INPUT diagnostic
    INPUT treatment
    INPUT payment_type

    IF age <= 0 OR charges < 0:
        DISPLAY "Invalid billing details"

    ELSE:

        total = consultation + diagnostic + treatment

        IF age >= 60:
            concession = total * 0.20

        ELSE IF age < 12:
            concession = total * 0.10

        ELSE:
            concession = 0

        final_bill = total - concession

        IF payment_type == "Insurance":
            final_bill = final_bill * 0.80

        ELSE IF payment_type == "Cash":
            category = "Self-Paying Patient"

        ELSE:
            DISPLAY "Invalid payment type"
            CONTINUE

        DISPLAY final_bill

        IF final_bill <= 1000:
            DISPLAY "Low"

        ELSE IF final_bill <= 5000:
            DISPLAY "Medium"

        ELSE:
            DISPLAY "High"

END FOR

STOP
7. Conclusion
The Hospital Patient Billing System calculates hospital charges, applies age-based concessions and insurance discounts, and classifies patients according to payment type. It also categorizes final bills using Python conditional statements and loops.

<img width="940" height="324" alt="image" src="https://github.com/user-attachments/assets/9a969863-a9cb-43c6-8d0c-996068b7186e" />

