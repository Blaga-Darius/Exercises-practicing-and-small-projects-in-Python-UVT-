#Write a program that reads an integer, N, and outputs all even numbers greater than 1 and less than N, including N if it is even.

n = int(input())

for i in range(2, n+1, 2):
    print(i)