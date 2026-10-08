#Given two lists of numbers, ln1, ln2 created before your code, execute the following operations:

#   insert value 10 in ln2 on position 0
#    pop the first value in ln1 and the last value in ln2
#    remove value 2 from ln1
#    print the index of 3 in ln1
#    print the number of occurrences of 5 in ln2
#    reverse list ln2
#    sort list ln1
#    extend ln1 with ln2
#    print ln1



n1 = int(input("Enter the number of elements in the first list: "))
ln1 = []
for i in range(n1):
    ln1.append(int(input("Enter an element for the first list: ")))

n2 = int(input("Enter the number of elements in the second list: "))
ln2 = []
for i in range(n2):
    ln2.append(int(input("Enter an element for the second list: ")))

ln1.append(3)
ln2.insert(0, 10)
ln1.pop(0)
i = len(ln2)-1
ln2.pop(i)
ln1.remove(2)
print(ln1.index(3))
print(ln2.count(5))
ln2.reverse()
ln1.sort()
print(ln1+ln2)