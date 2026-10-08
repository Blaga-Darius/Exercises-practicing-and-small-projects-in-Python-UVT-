#Print the sum of all even numbers strictly less than N — in ONE line, combining sum() and range().


n = int(input())
l = []

for i in range(2, n, 2):
    l.append(i)

print(sum(l))