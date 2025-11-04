## WAp to find sum of digits using recursion.

def sum_of_digits(n):
    if(n == 0):
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
    
number = int(input("Enter a number:"))
result = sum_of_digits(number)
print("Sum of digits is:",result)