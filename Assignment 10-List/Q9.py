#WAP having  number of elements  in the list and find out even and odd elements in that list and then create two seprate lists which will have even elements and other will have odd elements.

def seprate_even_odd(li):
    even_li = []
    odd_li = []
    for num in li:
        if(num % 2 == 0):
            even_li.append(num)
        else:
            odd_li.append(num)

    return even_li,odd_li
    
n = int(input("Enter number of elements:"))
numbers = []
for i in range(n):
    num = int(input("Enter element {i + 1}:"))
    numbers.append(num)

even,odds = seprate_even_odd(numbers)

print("Original list:",numbers)
print("Even numbers:",even)
print("Odd numbers:",odds)