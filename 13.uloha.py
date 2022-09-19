import math as math

a=int(input("Side a: "))
b=int(input("Side b: "))
c=int(input("Side c: "))

if (a+b)>c and (a+c)>b and (c+b)>a:
    print("The triangle does exist")
else:
    print("The triangle doesn't exist")

if (a+b)>c and (a+c)>b and (c+b)>a:
    alpha=((a**2-b**2-c**2)/(-(2*b*c)))
    alpha=math.acos(alpha)
    alpha=math.degrees(alpha)

    beta=((b**2-a**2+c**2)/(-(2*a*c)))
    beta=math.acos(beta)
    beta=math.degrees(beta)

    gamma=((c**2-a**2-b**2)/(-(2*a*b)))
    gamma=math.acos(gamma)
    gamma=math.degrees(gamma)
else:
    "The triangle doesn't exist"

if (a+b)>c and (a+c)>b and (c+b)>a:
    if alpha or beta or gamma ==90:
        print("The triangle is right")
    else:
        if alpha<90 and beta<90 or beta<90 and gamma<90 or alpha<90 and gamma<90:
            print("The triangle is acute ")
        else:
            if alpha>90 or beta>90 or gamma>90:
                print("The triangle is obtuse")
else:
    "The triangle doesn't exist"

if (a+b)>c and (b+c)>a and (c+a)>b:
    if gamma==beta==alpha:
        print("The triangle is equilateral")
    else:
        if alpha==beta or beta==gamma or alpha==gamma:
            print("The triangle is isosceles")
        else:
            print("The traingle is scalene")

