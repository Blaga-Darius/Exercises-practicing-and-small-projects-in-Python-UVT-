#Read a number, N, from standard input. Use list comprehension to create the list of all divisors of N (except 1 and N). 

n = int(input())
l = []

for i in range(2, n, 1):
    if n % i == 0:
        l.append(i)

print(l)