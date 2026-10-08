#Lists ln1 and ln2 are built before your code. Reverse ln1 in place, extend it with ln2, then print ln1.

n1 = int(input())
ln1 = []
for i in range(n1):     
    ln1.append(int(input()))

n2 = int(input())
ln2 = []
for i in range(n2):
    ln2.append(int(input()))

ln3 = ln1[::-1] + ln2
print(ln3)