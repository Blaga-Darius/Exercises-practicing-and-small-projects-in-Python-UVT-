#x and the list ln are built before your code; x appears at least once. Print how many times x appears, then its first position — no loops needed.

n = int(input("Enter the number of elements in the list: "))
ln = []
for i in range(n):
    ln.append(int(input("Enter an element: ")))

x = int(input("Enter the value to search for: "))

print(ln.count(x))
print(ln.index(x))