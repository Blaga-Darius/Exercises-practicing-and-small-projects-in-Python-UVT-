#Write a program that reads a number, N, from standard input and computes the sum of the first N natural numbers, including N.

n = int(input())
s = 0

while n > 0:
    s = s + n
    n = n - 1

print(s)