x = input("Give me a word: ")

a = len(x)

d = a//2
e = 0
for i in range (0,d):
    a-=1
    if x[i]==x[a]:
        e+=1

if e == d:
    print ("It's a palidrome")
else:
    print ("It isn't a palindome")