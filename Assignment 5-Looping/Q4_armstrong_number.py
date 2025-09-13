#Write a program to check if given number is Armstrong number or not.

num = int(input("Enter number:"))

power = len(str(num))
s = 0

for digit in str(num):
    s += int(digit) ** power
    
if(s == num):
    print(num, "is an armstrong number.")
else:
    print(num,"is not an armstrong number.")
