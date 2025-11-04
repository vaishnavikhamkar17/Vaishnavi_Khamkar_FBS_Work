# WAP to calaculate area of rectangle.

def area_rectangle(length,breadth):
    return  length * breadth

l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle:"))

area = area_rectangle(l,b)
print("Area of rectangle is :", area)