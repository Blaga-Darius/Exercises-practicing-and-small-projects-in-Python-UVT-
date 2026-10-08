#Given a list of strings, lw, print its length, then print the length of each string in the list.

n = int(input())
lw = []
for i in range(n):
    lw.append(input())

print(len(lw))

for w in lw:
    print(len(w))