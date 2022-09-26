x=int(input("x: "))
y=int(input("y: "))
count=0
for i in range(x,y+1):
    if i%8 == 0:
        count += 1
print(count)