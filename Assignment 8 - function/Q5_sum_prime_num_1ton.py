# Sum of all prime numbers from 1 to n .

def is_primes(num):
    if (n < 2) :
        return False
    for i in range(2, int(num**0.5) + 1):
        if (num % i == 0):
          return False
    return True

def sum_of_primes(n):
    total = 0
    for i in range(2, n + 1):
        if(is_primes(i)):
            total += i
    return total
    
n = int(input("Enter the value of n :"))
result = sum_of_primes(n)
print("Sum of all prime numbers from 1 to ",n,"=",result)
