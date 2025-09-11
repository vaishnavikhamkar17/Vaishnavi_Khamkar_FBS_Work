##WAP to print armstrong number within a given range.

start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

for num in range (start , end + 1):

    temp = num   # count digits
    count = 0
    while(temp > 0):
        count += 1
        temp //= 10

    temp = num     #calculate sum of digits
    sum_power = 0
    while(temp > 0):
        digit = temp % 10

        power = 1   #find digit ^ count using loop
        for i in range(count):
            power *= digit

        sum_power += power
        temp //= 10

    if(sum_power == num):
        print(num)

