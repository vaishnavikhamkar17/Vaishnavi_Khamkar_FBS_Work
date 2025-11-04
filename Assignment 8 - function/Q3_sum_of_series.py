#WAP to find sum of series using function

#1. 1 + 2 + 3 + 4 + ... + n

def sum_natural(n):
    return n * (n + 1) // 2

n = int(input("Enter value of n :"))
print("Sum of first", n, "natural numbers is :",sum_natural(n))

#2. 1! + 2! + 3! + 4! + .... + n!

def factorial(num):
    fact  = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total
n = int(input("ENter value of n :"))
print("Sum of factorials up to:", n, "iS", sum_factorials(n))

#3.1^1 + 2^2 + 3^3 +....n^n

def series_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i ** i
    return total

n = int(input("Enter value of n:"))
result = series_sum(n)
print("sum of series is :", result)