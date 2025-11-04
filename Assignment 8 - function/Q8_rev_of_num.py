#WAp to find reverse of number.

def reverse_of_num(num):
    rev = 0
    while(num > 0):
        digit = num % 10

        rev = rev * 10 + digit
        num = num // 10

    return rev

n = int(input("Enter a number:"))
result = reverse_of_num(n)
print("Reverse of",n,"is",result)