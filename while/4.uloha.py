n=int(input("Give me a number: "))
average=0
sum=0
count=0
while (n!=0):
    sum+=n
    n=int(input("Give me another number: "))
    count+=1
    average=float(sum/count)

print(average)
