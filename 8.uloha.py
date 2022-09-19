x=int(input("Input number: "))


z= x % 10
y= (x//10) % 10

print(y+z)


if (z+y) %2 == 0:
    print("The sum of last 2 digits of numbers is even")
else:
    print("The sum of last 2 digits of numbers isn't even")