## WAP to check if given number is strong number.

num = int(input("Enter a number:"))
temp = num
sum_fact= 0

while(temp > 0):
    digit = temp % 10

    fact = 1
    for i in range(1, digit+1):
          fact //= 10


if(sum_fact == num):
        print(num,"is a strong number.")
else:
     print(num,"is not a strong number.")