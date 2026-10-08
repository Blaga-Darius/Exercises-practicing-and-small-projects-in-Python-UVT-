#Write a program that reads a string from standard input and prints each character in the string, except spaces, using the for instruction.

s = input()

for l in s:
    if l != " ":
        print(l)