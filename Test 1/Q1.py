import math
l = int(input('Enter the length:'))
b = int(input('Enter the breadth:'))
r = int(input('Enter the radius:'))

Area_of_rectangle = l * b 
Area_of_Semicircle = (1/2) * math.pi * (r ** 2)
Total_Area = Area_of_rectangle + Area_of_Semicircle

perimeter = (2*l )+ b + math.pi * r

print(f'Area is: {Total_Area}')
print(f'perimeter is:{perimeter}')