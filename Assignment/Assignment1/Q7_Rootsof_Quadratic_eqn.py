##WAP to find Roots of quadratic equation.

a = int(input("Enter the coefficient a:"))
b = int(input("Enter the coefficient b:"))
c = int(input("Enter the coefficient c:"))

d = (b * b) - (4 * a * c)

if(d > 0):
    root1 = (-b + d ** 0.5)/(2 * a)
    root2 = (-b - d ** 0.5)/(2 * a)
    print("Roots are real and different.")
    print("Root 1=",root1)
    print("Root 2=",root2)
elif(d == 0):
    root = -b / (2 * a)
    print("Roots are real and equal.")
    print("Root =",root)
else:
    print("Roots are imaginary or complex.")

