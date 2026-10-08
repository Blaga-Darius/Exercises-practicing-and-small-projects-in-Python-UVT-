#Read a line of words. Print each word on its own line, but SKIP the words starting with '#' — use continue.

s = input()
b = 0

for w in s.split():
    b = 0
    for l in w:
        if l == "#":
            b = 1
            break
    if b == 0:
        print(w)