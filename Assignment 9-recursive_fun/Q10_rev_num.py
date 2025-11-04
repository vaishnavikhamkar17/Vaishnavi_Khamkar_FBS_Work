## WAP tp reverse number using recursion.

def reverse_number(num , rev=0):
    if(num == 0):
        return rev
    else: 
        rev = rev * 10 + num % 10
        return reverse_number(num // 10,rev)
    
number = int(input("Enter a number :"))
result = reverse_number(number)
print(f"Reversed number is:",result)