#Given a list of numbers, ln1, constructed before your code, print a new list which counts how many times each digit appears throughout all of the numbers from list ln1. 

n = int(input("Enter the number of elements in the list: "))
ln1 = []
for i in range(n):
    ln1.append(int(input("Enter an element for the list: ")))


ls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in ln1:
    for d in str(n):
        ls[int(d)] += 1

print(ls)
        