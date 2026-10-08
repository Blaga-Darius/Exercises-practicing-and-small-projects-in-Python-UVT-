#Write a program that reads an integer number from standard input and computes the sum of its digits.

a = int(input())
s  = 0

while a > 0:
    s = s + a%10
    a = a//10

print(s)  