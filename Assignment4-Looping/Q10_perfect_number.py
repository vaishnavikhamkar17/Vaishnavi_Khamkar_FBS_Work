## WAP to check if given number is perfect numbers.

num = int(input("Enter a number:"))

sum_of_divisiors = 0
i = 1
while(i < num):
    if(num % i == 0):
        sum_of_divisiors += i
    i += 1

if(sum_of_divisiors == num):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number.")