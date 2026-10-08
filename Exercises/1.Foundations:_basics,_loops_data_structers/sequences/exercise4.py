#The list ln is built before your code. Sort it in DESCENDING order and print it — one line for what would otherwise be a whole algorithm.

n = int(input())
ln = []
for i in range(n):
    ln.append(int(input())) 

ln.sort()
print(ln[::-1])