#Write a program that reads two numbers, a,ba,b, and outputs the one which is greater. If the numbers are equal, then the program should print the message "the numbers are equal".


a = int(input())
b = int(input())

if a>b:
    print(a)
elif  a < b:
    print(b)
else:
    print("the numbers are equal")