# WAP to check if a given number is armstrong number or not. For eacj task create seprae functions.

def count_digits(num):
    count = 0
    temp = num
    while(temp > 0):
        temp = temp // 10
        count += 1
    return count

def is_armstrong(num):
    n = count_digits(num)

    temp = num 
    sum_of_powers = 0
    while(temp > 0):
        digit = temp % 10
        sum_of_powers += digit ** n
        temp = temp // 10
    if(sum_of_powers == num):
        return True
    else:
        return False

number = int(input("Enter a number:"))
if is_armstrong(number):
    print(number, "is an armstrong number.")
else:
    print(number, "is not an armstrong number.")
