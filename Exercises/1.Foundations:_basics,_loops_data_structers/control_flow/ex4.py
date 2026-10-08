#Write a program that computes your grade for the Programming course:
#lab_grade = (test_1 + test_2)/2
#final_grade = 70% lab_grade + 30% exam_grade
#The input consists of three grades, for the first test, for the second test, and for the exam.
#If either the lab grade or the exam grade is less than 5, the program will print: "failed". Otherwise, the program will print the final grade.

n1 = float(input())
n2 = float(input())
ex = float(input())

nl = (n1 + n2)/2

if nl < 5 or ex < 5:
    print("failed")
else:
    print(f"{((nl/100)*70 + (ex/100)*30):.1f}")
