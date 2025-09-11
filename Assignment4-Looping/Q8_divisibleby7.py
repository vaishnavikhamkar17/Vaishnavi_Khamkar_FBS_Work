## WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

print("Numbers visible by 7 and multiple of 5 are:")

num = start
while(num <= end):
    if(num % 7 == 0 and num % 5 == 0):
        print(num)
    num += 1
