#WAP to find um of series using recursive function.
# 1!+ 2! + 3! + 4! + ...n!

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n -1)
    
def sum_of_factorials(n):
    if(n == 1):
        return 1
    else:
        return factorial(n)+sum_of_factorials(n - 1)
    
n = int(input("Enter value of n :"))
result = sum_of_factorials(n)
print("Sum of series is :",result)