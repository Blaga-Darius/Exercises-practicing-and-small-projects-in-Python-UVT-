#Read N and print all multiples of 7 from 7 up to N (inclusive), one per line — the step argument of range does it without any if.

n = int(input())

if n < 14 and n > 6:
    print(7)
else:
    for i in range(7, n, 7):
        print(i)