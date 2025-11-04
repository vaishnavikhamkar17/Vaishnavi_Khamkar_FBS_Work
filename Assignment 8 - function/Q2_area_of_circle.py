# WAP to calculate aera of circle.

def area_circle(radius):
    pi = 3.14                 # value of pi
    return 3.14 * radius * radius

r = int(input("Enter radius of circle:"))
area = area_circle(r)
print("Area of circle is :", area)