#WAP to check  if given number is armmstrong or not using recersive function.

def armstromg_sum(num,n):
    if (num == 0):
        return 0
    else:
        digit = num % 10
        return digit ** n + armstromg_sum(num // 10,n)

def is_armstrong(num):
    num_of_digits = len(str(num))
    return num == armstromg_sum(num,num_of_digits)

number = int(input("Enter a number :"))
if(is_armstrong(number)):
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not an armstrong number.")