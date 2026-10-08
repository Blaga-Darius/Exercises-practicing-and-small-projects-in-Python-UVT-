#Write a program that reads an integer number, N, and outputs True if N is a prime number, and False otherwise. A number is prime if its only divisors are 1 and N itself. You can use the break instruction to stop the loop early if the number is not prime.

n = int(input())

if n == 1:
    print("False")
elif n == 2:
    print("True")
else:
    for i in range(2, n):
        if n%i == 0:
            print("False")
            break
        if i == n//2:
            print("True")
            break
    

