Task1
University Scholarship Allocation System
1. Problem Statement
To develop a Python program that determines student scholarship eligibility based on aggregate marks, Mathematics marks, Physics marks, attendance, and annual family income. The program also assigns scholarship categories and calculates ranking scores for eligible students.
2. Objectives
1.	To collect student academic and personal details.
2.	To check scholarship eligibility using predefined conditions.
3.	To calculate the ranking score.
4.	To assign scholarship categories.
5.	To display reasons for ineligibility.
3. Assumptions
1.	Student name is entered as a string.
2.	Marks and attendance are entered as percentages.
3.	Aggregate marks must be at least 75%.
4.	Mathematics and Physics marks must be at least 60%.
5.	Attendance must be at least 75%.
6.	Annual family income must not exceed ₹2,50,000.
4. Algorithm
1.	Start the program.
2.	Accept student details as input.
3.	Check all eligibility conditions.
4.	If all conditions are satisfied, display the eligible message.
5.	Calculate the ranking score using aggregate marks and attendance.
6.	Assign Excellent, Merit, or General category.
7.	If conditions are not satisfied, display the reasons for ineligibility.
8.	Stop the program.
Test case
Test Case 1: Electricity Bill Calculation
Input:
Month 1 electricity units consumed: 10
Month 2 electricity units consumed: 10
Month 3 electricity units consumed: 10

Expected output:
Month 1 Bill: 67.45
Month 2 Bill: 67.45
Bill Decreased or Remained Same
Month 3 Bill: 67.45
Bill Decreased or Remained Same

Input:
•	Month 1 electricity units consumed: 10 
•	Month 2 electricity units consumed: 10 
•	Month 3 electricity units consumed: 10 
Expected Output:
•	Month 1 Bill: ₹67.45 
•	Month 2 Bill: ₹67.45 
•	Month 3 Bill: ₹67.45 
•	Bill Decreased or Remained Same 


Flow chart
<img width="940" height="1410" alt="image" src="https://github.com/user-attachments/assets/9471ff15-acd6-4593-bf34-591abb8591a8" />

 
6. Pseudocode
START

INPUT student_name
INPUT aggregate_marks
INPUT maths_marks
INPUT physics_marks
INPUT attendance
INPUT annual_income

IF aggregate >= 75 AND maths >= 60 AND
   physics >= 60 AND attendance >= 75 AND
   income <= 250000 THEN

    DISPLAY "Eligible"

    ranking_score = aggregate + attendance
    DISPLAY ranking_score

    IF aggregate >= 90 THEN
        DISPLAY "Excellent"
    ELSE IF aggregate >= 80 THEN
        DISPLAY "Merit"
    ELSE
        DISPLAY "General"
    END IF

ELSE
    DISPLAY "Not Eligible"

    CHECK each eligibility condition
    DISPLAY reasons for ineligibility

END IF

STOP
7. Conclusion
The program evaluates scholarship eligibility using Python conditional statements. It calculates ranking scores, assigns scholarship categories, and identifies reasons for ineligibility.
<img width="940" height="225" alt="image" src="https://github.com/user-attachments/assets/fa878684-6697-46d0-8aac-7c51755d0408" />


 
