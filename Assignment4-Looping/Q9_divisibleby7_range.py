##WAP to print all numbers in range divisible by given number.
start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))
divisior = int(input("Enter the number to check divisibility:"))

print("Numbers visible by 7 and multiple of 5 are:")

num = start
while(num <= end):
    if(num % divisior == 0):
        print(num)
    num += 1


