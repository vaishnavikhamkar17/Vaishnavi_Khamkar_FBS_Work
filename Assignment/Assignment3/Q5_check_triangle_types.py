## WAP to check wheather the triangle is equilateral, isosceles and scalene triangle.

a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side"))

if(a + b > c)or(a + c > b)or(b + c > a):
    if(a == b == c):
        print("The triangle is equilateral.")
    elif(a == b or b == c or a == c):
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The sides do not form a valid triangle")