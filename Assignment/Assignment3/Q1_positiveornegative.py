## WAp to check if the given number is positive or negative.

num = int(input("Enter the number:"))

if(num == 0):
    print(f"{num} is a neutral number.")
elif(num >= 0):
    print(f"{num} is a positive number.")
elif(num <= 0):
    print(f"{num} is a negative number.")