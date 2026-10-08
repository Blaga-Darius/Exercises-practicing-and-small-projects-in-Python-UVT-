#Write a program that reads a number, N, from standard input and prints all its divisors, except for 1 and N.

n = int(input())
i = 2

while i < n:
    if n%i == 0:
        print(i)
    i = i + 1