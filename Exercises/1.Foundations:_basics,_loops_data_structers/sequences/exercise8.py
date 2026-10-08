#Given two lists of numbers, ln1, ln2, constructed before your code, print all elements from ln1 that also appear in ln2.

n1 = int(input("Enter the number of elements in the first list: "))
ln1 = []
for i in range(n1):
    ln1.append(int(input("Enter an element for the first list: ")))

n2 = int(input("Enter the number of elements in the second list: "))
ln2 = []
for i in range(n2):
    ln2.append(int(input("Enter an element for the second list: ")))

for i in ln1:
    for j in ln2:
        if i == j:
            print(i)