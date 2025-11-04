###WAp to reverse a given number using recursive function.

def reverse_number(num,rev=0):
    if(num == 0):
        return rev
    else:
        rev = rev * 10 + num % 10
        return reverse_number(num // 10,rev)

number = int(input("Enter a number:"))
reversed_number = reverse_number(number)
print(f"The reverse of {number} is {reversed_number} .")    