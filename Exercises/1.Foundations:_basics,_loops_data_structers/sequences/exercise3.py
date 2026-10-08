#Given a list of numbers, ln, created before your code, print all elements on even positions (0 included).

n = int(input())
ln = []
for i in range(n):
    ln.append(int(input()))


for i in range (0, n, 2):
    print(ln[i])