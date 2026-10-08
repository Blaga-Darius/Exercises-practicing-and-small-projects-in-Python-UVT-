#Modify the following code such that it only prints the message "Found" once.

word = input()
s = input()
for x in word:
    if s == x:
        print("Found")
        break