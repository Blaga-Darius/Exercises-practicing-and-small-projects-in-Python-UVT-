#Write a program that allows you to calculate the BMI (Body Mass Index) of a person. The body mass index is calculated using the formula: BMI = weight / (height * height)
#The program should read the mass (in kg) and the height (in metres, for example: 1.76) and output the corresponding message from the table.

m = float(input())
h = float(input())

bmi = m/(h*h)

if bmi < 18.5:
    print("High risk: the weight is too low")
elif bmi >= 18.5 and bmi < 25:
    print("Minimum/Low risk")
elif bmi >= 25 and bmi < 30:
    print("Low/Medium risk")
elif bmi >= 30 and bmi < 35:
    print("Medium/High risk")
else:
    print("High risk: the weight is too high")