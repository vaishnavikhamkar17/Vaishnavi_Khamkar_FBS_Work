## WAP to calculate the m to the power n using recursion.

def power(m,n):
    if(n == 0):
        return 1
    elif(n > 0):
        return m * power(m,n - 1)
    else:
        return 1 / power(m, -n)

base = int(input("Enter the base(m):"))
exponent = int(input("Enter the exponent(n):"))
result = power(base,exponent)
print(f"{base} to the power {exponent} is {result}.")
