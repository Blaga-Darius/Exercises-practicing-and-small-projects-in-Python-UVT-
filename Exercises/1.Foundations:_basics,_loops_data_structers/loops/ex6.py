#Read N and print the numbers from N down to 1, one per line — use range with a negative step.

n = int(input())

for i in range(n, 0, -1):
    print(i)