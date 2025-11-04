## WAp to find sum of n munbers using recursion.

def sum_of_n(n):
    if (n == 0):
        return 0
    else:
        return n + sum_of_n(n - 1)
    
number = int(input("Enter a number:"))
total = sum_of_n(number)
print(f"Sum of first {number} is {total} .2")