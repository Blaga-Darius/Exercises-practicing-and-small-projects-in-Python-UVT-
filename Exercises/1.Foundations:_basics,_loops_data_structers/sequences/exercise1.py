#Write a program that reads a number, N, and then reads N lines representing words. The program will add each word to a list which will be printed after reading all words. 

l = []
n = int(input())

for i in range(n):
    l.append(input())

print(l)