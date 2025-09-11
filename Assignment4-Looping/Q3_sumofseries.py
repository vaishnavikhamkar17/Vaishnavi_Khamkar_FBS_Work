#WAP to print sum of series upto n.
n = int(input("Enter the value of n:"))
i =1
seris_sum = 0

while(i <= n):
    seris_sum  += i
    i += 1
    print("Sum of series=",seris_sum)