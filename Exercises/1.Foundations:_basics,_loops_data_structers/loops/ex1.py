#Read a natural number n ≥ 1. Using a while loop, print how many times n can be halved (integer division by 2) until it reaches 0.

a = int(input())
b = 0

while a > 0:
    a = a // 2
    b = b + 1

print(b)