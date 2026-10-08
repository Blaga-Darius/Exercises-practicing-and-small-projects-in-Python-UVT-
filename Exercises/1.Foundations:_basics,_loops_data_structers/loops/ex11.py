#Read n > 1. Print the SMALLEST divisor of n greater than 1, using break to stop the search as soon as it is found.


n = int(input())

for i in range(2, n+1):
    if n % i == 0:
        print(i)
        break
    