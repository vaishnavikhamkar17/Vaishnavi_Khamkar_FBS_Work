## WAp to check wheather a number is prime or not using recursion.

def is_prime(n , i = 2):
    if(n <= 0):
        return False
    if(i * i > n):
        return True
    if(n % i == 0):
        return False
    return is_prime(n , i + 1)

number = int(input("Enter a number:"))

if(is_prime(number)):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")