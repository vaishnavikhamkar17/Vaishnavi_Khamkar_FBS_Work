##WAP to input two angles from user and find third angle of triangle. 

x = int(input("Enter angle 1:"))
y = int(input("Enter angle 2:"))

Third_angle =  180 - (x+y)

print(f"Third angle is:{Third_angle}")