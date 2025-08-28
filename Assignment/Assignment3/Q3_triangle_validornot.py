##WAP to input angles of triangle and check wheather triangle is valid or not.

angle_1 = int(input("Enter the angle1:"))
angle_2 = int(input("Enter the angle2:"))
angle_3 = int(input("Enter the angle3:"))

if(angle_1 + angle_2 + angle_3 == 180):
    print(f"The triangle is valid")
else:
    print(f" The triangle is not valid")